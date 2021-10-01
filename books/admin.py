from django.contrib import admin
from books.models import Book, Page, UserProfileInfo, UserBook, UserBookBookmark, UserReadBook

admin.site.site_header = 'KnowledgeIsPower Admin'
admin.site.site_title = 'KnowledgeIsPower Admin Area'
admin.site.index_title = 'Welcome to the KnowledgeIsPower admin area'


# Register your models here.
admin.site.register(Book)
admin.site.register(Page)
admin.site.register(UserProfileInfo)
admin.site.register(UserBook)
admin.site.register(UserBookBookmark)
admin.site.register(UserReadBook)