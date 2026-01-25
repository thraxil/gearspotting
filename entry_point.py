import os
import sys

def main():
    app_name = os.environ.get("APP", "gearspotting")
    port = os.environ.get("PORT", "8000")

    if settings := os.environ.get("SETTINGS"):
        os.environ["DJANGO_SETTINGS_MODULE"] = f"{app_name}.{settings}"
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{app_name}.settings_docker")

    args = sys.argv[1:]
    if not args:
        return

    command = args[0]

    if command == "migrate":
        print("running migrations")
        cmd_args = ["uv", "run", "manage.py", "migrate"]
    elif command == "collectstatic":
        cmd_args = ["uv", "run", "manage.py", "collectstatic", "--verbosity", "2", "--noinput"]
    elif command == "shell":
        cmd_args = ["uv", "run", "manage.py", "shell"]
    elif command == "manage":
        cmd_args = ["uv", "run", "manage.py"] + args[1:]
    elif command == "run":
        cmd_args = [
            "uv", "run", "gunicorn",
            "--env", f"DJANGO_SETTINGS_MODULE={os.environ['DJANGO_SETTINGS_MODULE']}",
            f"{app_name}.wsgi:application",
            "-b", f"0.0.0.0:{port}",
            "-w", "3",
            "--max-requests=1000",
            "--max-requests-jitter=50",
            "--access-logfile=-",
            "--error-logfile=-",
        ]
    else:
        return

    os.execvp(cmd_args[0], cmd_args)

if __name__ == "__main__":
    main()
