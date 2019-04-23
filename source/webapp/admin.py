from django.contrib import admin
from django.contrib.auth.models import User
from webapp.models import UserInfo, Skill, Program, Session, Result, Child, Categories
from django.contrib.auth.admin import UserAdmin


class ResultModelAdmin(admin.ModelAdmin):
    list_display = ['session_id', 'code_skill']
    search_fields = ['session_id', 'code_skill']
    list_filter = ['created_date', 'edited_date']

    def session_id(self, obj):
        return obj.session.pk
    session_id.empty_value_display = 'Не известно'

    def code_skill(self, obj):
        return obj.skill.code_skill
    code_skill.empty_value_display = 'Не известно'


class SessionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'program_name', 'created_date', 'child_name']
    search_fields = ['program_name', 'child_name']
    list_filter = ['created_date', 'edited_date']

    def child_name(self, obj):
        return obj.child.first_name
    child_name.empty_value_display = 'Не известно'

    def program_name(self, obj):
        return obj.program.name
    program_name.empty_value_display = 'Не известно'


class ProgramModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['created_date', 'edited_date']
    filter_horizontal = ('skill',)


class SkillModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'code_skill']
    search_fields = ['name', 'code_skill']
    list_filter = ['created_date', 'updated_date']


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'code_category']
    search_fields = ['name']
    list_filter = ['created_date', 'edited_date', 'code_category']


class ChildrenModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "age", "first_parent"]
    search_fields = ["first_name"]
    list_filter = ['created_date', 'edited_date']


class InlineUser(admin.StackedInline):
    model = UserInfo


class UserInfoAdmin(UserAdmin):
    inlines = [InlineUser, ]
    search_fields = ['username']


admin.site.site_header = 'Administrate your website'
admin.site.unregister(User)
admin.site.register(User, UserInfoAdmin)
admin.site.register(Skill, SkillModelAdmin)
admin.site.register(Program, ProgramModelAdmin)
admin.site.register(Session, SessionModelAdmin)
admin.site.register(Result, ResultModelAdmin)
admin.site.register(Child, ChildrenModelAdmin)
admin.site.register(Categories, CategoryModelAdmin)
