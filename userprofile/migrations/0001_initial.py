# Generated by Django 2.1 on 2018-09-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.IntegerField(choices=[(1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], default=2018, verbose_name='Year')),
                ('Name', models.CharField(max_length=30)),
                ('Title', models.CharField(max_length=30)),
                ('Info', models.CharField(max_length=1500)),
                ('Picture', models.ImageField(help_text="If you receive an error on saving Images, Please go back and Re-upload and Try Again. png Images work but jpeg's are recommended", upload_to='')),
                ('Twitter_URL', models.URLField(blank=True)),
                ('Facebook_URL', models.URLField(blank=True)),
                ('Profile_URL', models.URLField(blank=True)),
                ('LinkedIn_URL', models.URLField(blank=True)),
                ('UserType', models.CharField(choices=[('Board', 'Board'), ('Staff', 'Staff'), ('Intern', 'Intern'), ('Fellow', 'Fellow')], max_length=20)),
            ],
        ),
    ]
