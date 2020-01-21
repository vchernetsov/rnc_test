CREATE USER butter_user with encrypted password '3bbqu2sebx';
CREATE DATABASE butter_db;
ALTER DATABASE butter_db OWNER TO butter_user;
GRANT ALL PRIVILEGES ON DATABASE butter_db TO butter_user;
ALTER USER butter_user CREATEDB;
