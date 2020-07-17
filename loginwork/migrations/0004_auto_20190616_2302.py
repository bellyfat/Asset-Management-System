# Generated by Django 2.2.2 on 2019-06-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginwork', '0003_purchaseassetmap_purchaserecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='assetstable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelno', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=100)),
                ('productno', models.CharField(max_length=100)),
                ('purchaseno', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='elementstable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elementtype', models.CharField(max_length=100)),
                ('assetid', models.CharField(max_length=100)),
                ('slno', models.CharField(max_length=100)),
                ('ctno', models.CharField(max_length=100)),
                ('spno', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='purchasestable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaseno', models.CharField(max_length=100)),
                ('serialno', models.CharField(max_length=100)),
                ('warrantystartdate', models.CharField(max_length=100)),
                ('warrantyenddate', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userstable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('employeeid', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='assettable',
        ),
        migrations.DeleteModel(
            name='cpufantable',
        ),
        migrations.DeleteModel(
            name='dvdrwdrivetable',
        ),
        migrations.DeleteModel(
            name='frontpanelswitchtable',
        ),
        migrations.DeleteModel(
            name='graphicscardtable',
        ),
        migrations.DeleteModel(
            name='hddtable',
        ),
        migrations.DeleteModel(
            name='keyboardtable',
        ),
        migrations.DeleteModel(
            name='mbdtable',
        ),
        migrations.DeleteModel(
            name='memorytable',
        ),
        migrations.DeleteModel(
            name='monitortable',
        ),
        migrations.DeleteModel(
            name='mousetable',
        ),
        migrations.DeleteModel(
            name='processortable',
        ),
        migrations.DeleteModel(
            name='purchaseassetmap',
        ),
        migrations.DeleteModel(
            name='purchaserecord',
        ),
        migrations.DeleteModel(
            name='purchasetable',
        ),
        migrations.DeleteModel(
            name='sascardtable',
        ),
        migrations.DeleteModel(
            name='smpstable',
        ),
        migrations.DeleteModel(
            name='systemfantable',
        ),
        migrations.DeleteModel(
            name='userlogin',
        ),
        migrations.DeleteModel(
            name='usertable',
        ),
    ]
