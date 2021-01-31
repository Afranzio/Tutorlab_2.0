from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_id = models.CharField(max_length=200)
    phone = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=250, null=True)
    role = models.CharField(max_length=150)
    seek_skills = models.CharField(max_length=150, null=True)
    teach_skills = models.CharField(max_length=150, null=True)
    country = models.CharField(max_length=150, null=True)
    rate = models.IntegerField(null=True)
    rating = models.CharField(max_length=150, null=True)
    level = models.CharField(max_length=150, null=True)
    Languages = models.CharField(max_length=150, null=True)
    password = models.CharField(max_length=150, null=True)


class Class(models.Model):
    student_id = models.CharField(max_length=150)
    class_id = models.AutoField(primary_key=True)
    class_details = models.CharField(max_length=150, null=True)
    classe_name = models.CharField(max_length=150)


class Connect(models.Model):
    connect_id = models.AutoField(primary_key=True)   
    class_id = models.CharField(max_length=150)
    student_id = models.ForeignKey('Class',models.DO_NOTHING, blank=True, null=True)
    teacher_id = models.CharField(max_length=150)
    connect_status = models.CharField(max_length=150, null=True)
    connect_seek_rating = models.CharField(max_length=150, null=True)
    connect_teach_rating = models.CharField(max_length=150, null=True)
    connect_rate =  models.CharField(max_length=150, null=True)

class Connect_Message(models.Model):
    connect_message_id = models.AutoField(primary_key=True)
    connect_id = models.ForeignKey('Connect',models.DO_NOTHING, blank=True, null=True)
    connect_message_ts = models.DateTimeField()
    connect_message_text = models.TextField()
    connect_message_user_id = models.ForeignKey('User',models.DO_NOTHING, blank=True, null=True)
    Is_Read = models.BooleanField() 

class Connect_Message_Attach(models.Model):
    connect_message_id = models.CharField(max_length=60)
    connect_attach_file_blob = models.CharField(max_length=60, null=True)
    connect_attach_file_type = models.CharField(max_length=60, null=True)

class level(models.Model):
    level_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=60, null=True)

class country(models.Model):
    country_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=60, null=True)

class city(models.Model):
    city_id = models.AutoField(primary_key=True)
    country_id = models.ForeignKey('country',models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=60, null=True)

class rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=60, null=True)

class connect_status(models.Model):
    connect_status_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=60, null=True)



