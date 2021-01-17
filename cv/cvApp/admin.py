from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'selfName', 'title', 'text', 'get_photo')
    list_display_links = ('id', 'selfName')
    fields = ('selfName', 'title', 'text', 'quote', 'image', 'get_photo')
    readonly_fields = ('get_photo',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return 'Фото не установлено'

    get_photo.short_description = 'Миниатюра'


class AllImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_startImg', 'get_skillImg', 'get_contactImg')
    list_display_links = ('id', 'get_startImg', 'get_skillImg', 'get_contactImg')
    fields = ('startImg', 'get_startImg', 'skillImg', 'get_skillImg', 'contactImg', 'get_contactImg')
    readonly_fields = ('get_startImg', 'get_skillImg', 'get_contactImg')

    def get_startImg(self, obj):
        if obj.startImg:
            return mark_safe(f'<img src="{obj.startImg.url}" width="75">')
        else:
            return 'Фото не установлено'

    def get_skillImg(self, obj):
        if obj.skillImg:
            return mark_safe(f'<img src="{obj.skillImg.url}" width="75">')
        else:
            return 'Фото не установлено'

    def get_contactImg(self, obj):
        if obj.contactImg:
            return mark_safe(f'<img src="{obj.contactImg.url}" width="75">')
        else:
            return 'Фото не установлено'

    get_startImg.short_description = 'Миниатюра стартовой картинки'
    get_skillImg.short_description = 'Миниатюра картинки способностей'
    get_contactImg.short_description = 'Миниатюра картинки контактов'


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'email', 'phone')
    list_display_links = ('id', 'address', 'email', 'phone')


class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'job', 'post')
    list_display_links = ('id', 'year', 'job', 'post')


class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'client', 'category', 'skill', 'liveurl', 'get_photo', 'get_pic')
    list_display_links = ('id', 'title', 'get_photo')
    fields = ('title', 'description', 'date', 'client', 'category', 'skill', 'liveurl', 'image', 'get_photo', 'pic', 'get_pic')
    readonly_fields = ('get_photo', 'get_pic')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return 'Фото не установлено'

    def get_pic(self, obj):
        if obj.pic:
            return mark_safe(f'<img src="{obj.pic.url}" width="100">')
        else:
            return 'Фото не установлено'

    get_photo.short_description = 'Миниатюра'
    get_pic.short_description = 'Фото'


class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link')
    list_display_links = ('id', 'title')

    # def get_icon(self, obj): TODO: Вывести иконку социальной сети. В админке нет font-awesome
    #     return mark_safe(f'<i class="fa fa-{obj.title}"></i>')


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'percent')
    list_display_links = ('id', 'title', 'percent')


admin.site.register(About, AboutAdmin)
admin.site.register(Knowledge)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Contacts, ContactAdmin)
admin.site.register(AllImg, AllImgAdmin)
admin.site.register(SocialLinks, SocialLinksAdmin)
