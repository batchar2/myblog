from django.contrib import admin

from .models import Post, Category, Tag, SitePage


# Статические файлы
#from django.core.files.storage import DefaultStorage
#from filebrowser.sites import FileBrowserSite

#from django.core.files.storage import FileSystemStorage
#site.storage = FileSystemStorage(location='uppload', base_url='/media/')

# Default FileBrowser site
#site = FileBrowserSite(name='filebrowser', storage=DefaultStorage())
#
# My Custom FileBrowser site
#custom_site = FileBrowserSite(name='custom_filebrowser', storage=DefaultStorage())
#custom_site.directory = "uploads/"
#
#admin.site.register(site)

"""
Управление блогом
"""
class PostAdmin(admin.ModelAdmin):
    # Поле slug будет заполнено на основе поля title
    prepopulated_fields = {'slug': ('title',)}
    # Отображающиеся в списке поля
    list_display = ('title', 'published_date', 'is_publish', 'slug')
    # Поля фильтра
    list_filter = ('published_date', 'is_publish', 'title')
    # Поиск пополям
    search_fields = ('title', 'content')
    # определяем иерархию по дате
    #date_hierarchy = 'published_date'

class CategoryAdmin(admin.ModelAdmin):
     # Поле slug будет заполнено на основе поля title
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'is_publish', 'slug')

class TagAdmin(admin.ModelAdmin):
    # Поле slug будет заполнено на основе поля title
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'is_publish', 'slug')

class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'url',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(SitePage, PageAdmin)
"""
Управление сайтом
"""
#from .models import SitePage, MenuItem, PageMenuItem, StaticURLPageMenuItem

#admin.site.register(SitePage)
#admin.site.register(MenuItem)
#admin.site.register(PageMenuItem)
#admin.site.register(StaticURLPageMenuItem)

