# Generated by Django 5.1.1 on 2024-10-01 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_userprofile_facebook_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='batch_year',
            field=models.IntegerField(choices=[(2028, 2028), (2027, 2027), (2026, 2026), (2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987)], default=2024),
        ),
    ]