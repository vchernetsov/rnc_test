FROM python:3.7
ARG BUILD_FOR
RUN pip install --upgrade pip
WORKDIR /usr/src/app/
ADD . /usr/src/app/
RUN pip install -r requirements/base.txt
RUN pip install -r requirements/${BUILD_FOR}.txt
