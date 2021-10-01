import django


django.setup()

from accounts.models import CustomUser
from core.db_models.faculty_db_model import Faculty

# How to run:
# python manage.py shell
# exec(open('deploy_script.py').read())


if not CustomUser.objects.filter(username='admin').exists():
    CustomUser.objects.create_superuser(
        username='admin',
        password='H6r3Lh\D#-~PcMQ6',
    )

FACULTY = [
    {
        'name': 'faculty1'
    },
    {
        'name': 'faculty2'
    },
    {
        'name': 'faculty3'
    },
    {
        'name': 'faculty4'
    },
]

for f in FACULTY:
    if not Faculty.objects.filter(name=f['name']).exists():
        Faculty.objects.create(name=f['name'])
