from fabric.api import run, sudo, local, cd, env

env.hosts = ['maru.thraxil.org']
env.user = 'anders'
nginx_hosts = ['lolrus.thraxil.org']

def restart_gunicorn():
    sudo("restart gearspotting")

def prepare_deploy():
    local("./manage.py test")

def deploy():
    code_dir = "/var/www/gearspotting/gearspotting"
    with cd(code_dir):
        run("git pull origin master")
        run("./bootstrap.py")
        run("./manage.py migrate")
        run("./manage.py collectstatic --noinput --settings=gearspotting.settings_production")
        for n in nginx_hosts:
            run(("rsync -avp --delete media/ "
                 "%s:/var/www/gearspotting/gearspotting/media/") % n)

    restart_gunicorn()
