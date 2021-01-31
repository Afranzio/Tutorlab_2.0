from django.contrib import admin
from .models import User,Class,Connect,Connect_Message,Connect_Message_Attach

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['user_id','first_name','last_name','email_id','phone','address','role','seek_skills','teach_skills','country','rate','rating','level','Languages']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display=['student_id','class_id','class_details','classe_name']

@admin.register(Connect)
class ConnectAdmin(admin.ModelAdmin):
    list_display=['connect_id','class_id','student_id','teacher_id','connect_status','connect_seek_rating','connect_teach_rating','connect_rate']

@admin.register(Connect_Message)
class Connect_MessageAdmin(admin.ModelAdmin):
    list_display = ['connect_message_id','connect_id','connect_message_ts','connect_message_text','connect_message_user_id','Is_Read']

@admin.register(Connect_Message_Attach)
class Connect_Message_AttachAdmin(admin.ModelAdmin):
     list_display = ['connect_message_id','connect_attach_file_blob','connect_attach_file_type']