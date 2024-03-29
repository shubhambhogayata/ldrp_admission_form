# Generated by Django 4.1.4 on 2023-06-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="formTable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ACPCRank", models.CharField(max_length=100)),
                ("DOB", models.DateField()),
                ("GUJCETRollNo", models.CharField(max_length=100)),
                ("POB", models.CharField(max_length=100)),
                ("bloodGroup", models.CharField(max_length=100)),
                ("board", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("city3", models.CharField(max_length=100)),
                ("cityOfPermanentAddress", models.CharField(max_length=1000)),
                ("course", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("fatherName", models.CharField(max_length=100)),
                ("fatherName2", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=100)),
                ("grandFatherName", models.CharField(max_length=100)),
                ("gujcetBoard", models.CharField(max_length=100)),
                ("gujcetClass", models.CharField(max_length=100)),
                ("gujcetMark", models.CharField(max_length=100)),
                ("gujcetPecentile", models.CharField(max_length=100)),
                ("gujcetPercentage", models.CharField(max_length=100)),
                ("gujcetYear", models.CharField(max_length=100)),
                ("hscBoard", models.CharField(max_length=100)),
                ("hscClass", models.CharField(max_length=100)),
                ("hscMark", models.CharField(max_length=100)),
                ("hscPecentile", models.CharField(max_length=100)),
                ("hscPercentage", models.CharField(max_length=100)),
                ("hscYear", models.CharField(max_length=100)),
                ("hscAllBoard", models.CharField(max_length=100)),
                ("hscAllClass", models.CharField(max_length=100)),
                ("hscAllMark", models.CharField(max_length=100)),
                ("hscAllPecentile", models.CharField(max_length=100)),
                ("hscAllPercentage", models.CharField(max_length=100)),
                ("hscAllYear", models.CharField(max_length=100)),
                ("localAddress", models.CharField(max_length=1000)),
                ("medium", models.CharField(max_length=100)),
                ("motherName", models.CharField(max_length=100)),
                ("nameOfSchool", models.CharField(max_length=100)),
                ("nameOfTheStudent", models.CharField(max_length=100)),
                ("parentMobileNo", models.CharField(max_length=100)),
                ("parentOccupation", models.CharField(max_length=100)),
                ("parentOccupationAddress", models.CharField(max_length=1000)),
                ("passportPhoto", models.CharField(max_length=100)),
                ("passportPhotoName", models.CharField(max_length=100)),
                ("permanentAddress", models.CharField(max_length=1000)),
                ("pinCode", models.CharField(max_length=100)),
                ("pinCode3", models.CharField(max_length=100)),
                ("pinCodeOfPermanentAddress", models.CharField(max_length=100)),
                ("religion", models.CharField(max_length=100)),
                ("round", models.CharField(max_length=100)),
                ("signOfParent", models.CharField(max_length=100)),
                ("signOfParentName", models.CharField(max_length=100)),
                ("signOfStudent", models.CharField(max_length=100)),
                ("signOfStudentName", models.CharField(max_length=100)),
                ("sscBoard", models.CharField(max_length=100)),
                ("sscClass", models.CharField(max_length=100)),
                ("sscMark", models.CharField(max_length=100)),
                ("sscPecentile", models.CharField(max_length=100)),
                ("sscPercentage", models.CharField(max_length=100)),
                ("sscYear", models.CharField(max_length=100)),
                ("studentEmail", models.CharField(max_length=100)),
                ("studentMobileNo1", models.CharField(max_length=100)),
                ("studentMobileNo2", models.CharField(max_length=100)),
                ("studentName", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                ("surname2", models.CharField(max_length=100)),
            ],
        ),
    ]
