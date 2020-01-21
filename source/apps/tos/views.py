import os
from django.shortcuts import render
from django.utils.timezone import now as tz_now
from apps.tos import forms
from apps.tos import models
from django.template.loader import render_to_string
from rest_framework.exceptions import MethodNotAllowed
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
import ntpath
import zlib
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def sign_view(request):
    now = tz_now()
    context = {
        "timestamp": now,
        "user": request.user,
    }
    text = render_to_string('agreements/current.html', context)
    text = text.replace("\r\n", "\n")
    text = text.strip()
    data = {
        "text": text,
        "signature": forms.signer.get_signature(text).decode(),
        "timestamp": now,
        # TODO: protect timestamp by signature too
    }
    context['form'] = forms.ToSForm(data=data)
    context['text'] = text
    return render(request, 'agreements/base.html', context)

@staff_member_required
def sign_view_action(request):
    if request.method != 'POST':
        raise MethodNotAllowed(request.method)
    form = forms.ToSForm(request.POST)
    if form.is_valid():
        entry = models.SignedTOS()
        entry.user = request.user
        entry.first_name = request.user.first_name
        entry.last_name = request.user.last_name
        entry.street = request.user.street
        entry.post_code = request.user.post_code
        entry.created_at = form.cleaned_data['timestamp']
        filename = models.signed_file_path(instance=entry, filename="signed_file.html")
        entry.signed_file = filename
        absname = os.path.join(settings.MEDIA_ROOT, filename)
        abspath = ntpath.dirname(absname)
        os.makedirs(abspath)
        with open(absname, "wb") as fh:
            compressed = zlib.compress(form.cleaned_data['text'].encode())
#            fh.write(form.cleaned_data['text'])
            fh.write(compressed)

        entry.save()
        messages.success(request, 'Tos signed!')
    else:
        for error in form.errors:
            messages.error(request, error)
    return redirect('admin:index')
