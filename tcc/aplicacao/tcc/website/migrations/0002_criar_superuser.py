from django.db import migrations
from django.contrib.auth import get_user_model

def criar_superusuario(apps, schema_editor):
    User = get_user_model()
    if not User.objects.filter(email='admin@admin.com').exists():
        User.objects.create_superuser(
            email='admin@admin.com',
            username='admin',
            password='admin123',
        )

class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_superusuario),
    ]