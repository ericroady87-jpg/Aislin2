from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_weapons_alter_fueling_options_alter_fueling_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='MS',
            name='Weapons',
            field=models.ManyToManyField(to='main_app.Weapons'),
        ),
    ]