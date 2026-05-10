from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_fueling'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='fueling',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='fueling',
            name='date',
            field=models.DateField(verbose_name='Fueling Date'),
        ),
    ]