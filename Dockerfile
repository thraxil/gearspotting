FROM ubuntu:trusty
RUN apt-get update
RUN apt-get install python-ldap libldap2-dev libsasl2-dev \
    python-all-dev libxml2-dev libxslt1-dev libjpeg-dev \
    python-tk liblcms1 libexif-dev libexif12 libfontconfig1-dev \
    libfreetype6-dev liblcms1-dev libxft-dev python-imaging \
    python-beautifulsoup python-dev libssl-dev gcc \
    build-essential binutils libpq-dev postgresql-client python-pip \
    -y
ENV PYTHONUNBUFFERED 1
RUN apt-get install nodejs npm -y
RUN ln -s /usr/bin/nodejs /usr/local/bin/node
RUN mkdir -p /var/www/gearspotting
COPY requirements.txt /var/www/gearspotting/gearspotting/
RUN pip install -r /var/www/gearspotting/gearspotting/requirements.txt
WORKDIR /var/www/gearspotting/gearspotting
COPY . /var/www/gearspotting/gearspotting/
RUN python manage.py test
EXPOSE 8000
ADD docker-run.sh /run.sh
CMD /run.sh
