import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fueling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fuel_type', models.CharField(choices=[('N', 'Nuclear'), ('P', 'Propellant'), ('G', 'GN particles')], default='P', max_length=2)),
                ('ms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.mobile_suit')),
            ],
        ),
    ]