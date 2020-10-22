import os
import datetime
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git_commit():
    now = datetime.datetime.now()
    now = str(now.strftime("%Y-%m-%d %H:%M"))
    user_name = os.getenv("GITLAB_NAME", settings.CONFIG_DATA.get("GITLAB_NAME"))
    user_password = os.getenv("GITLAB_PASSWORD", settings.CONFIG_DATA.get("GITLAB_PASSWORD"))
    mail = os.getenv("GMAIL", settings.CONFIG_DATA.get("GMAIL"))
    os.chdir(BASE_DIR)
    os.system(f"git config --local user.email {mail}")
    os.system(f"git config --local user.name {user_name}")
    os.system("git remote rm origin")
    os.system(f"git remote add origin https://{user_name}:{user_password}@gitlab.com/finlab_company_class/tw_stock.git")
    os.system("git pull origin master")
    os.system("git add data/")
    os.system("git commit -m '%s update data'" % now)
    os.system("git push -u origin master")
    info = "Finish!git push successfully"
    return info
