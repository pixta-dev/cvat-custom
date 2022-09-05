# Generated by Django 3.2.15 on 2022-09-05 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        ('engine', '0059_labeledshape_outside'),
        ('webhooks', '0002_auto_20220812_1259'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='webhook',
            unique_together={('target_url', 'secret', 'enable_ssl', 'type', 'content_type', 'events', 'project_id'), ('target_url', 'secret', 'enable_ssl', 'type', 'content_type', 'events', 'organization_id')},
        ),
    ]