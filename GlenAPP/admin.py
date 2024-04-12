from django.contrib import admin

# Register your models here.

from django.contrib import admin
from GlenAPP.models import UserInfo,Subject,Teacher,Question,Choice

admin.site.site_header = '任务管理系统'


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password',)
    list_display_links = ('username',)
    list_per_page = 50

class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('no','name','intro','is_hot')
    search_fields = ('name',)
    ordering = ('no',)

class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'good_count', 'bad_count', 'subject')
    search_fields = ('name', )
    ordering = ('no', )

class GlenQuestion(admin.ModelAdmin):
    list_display = ('question_text','pub_date')
    search_fields=('question_text',)



admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Subject,SubjectModelAdmin)
admin.site.register(Teacher,TeacherModelAdmin)
admin.site.register(Question,GlenQuestion)


