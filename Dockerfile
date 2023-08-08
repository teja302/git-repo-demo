FROM ubuntu
RUN apt-get update
RUN apt-get install -y apache2
ADD file1.py /var/www/html
ENTRYPOINT apachectl -D FOREGROUND

