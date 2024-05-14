# Generated by Django 4.2.2 on 2023-09-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0006_alter_leave_leavetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='leavetype',
            field=models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'CL(First Half)'), ('casual', 'CL(Second Half)'), ('casual', 'CL(Full Day)'), ('emergency', 'Medical Leave')], default='sick', max_length=25, null=True),
        ),
    ]
