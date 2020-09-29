from django.contrib import admin
from .models import Author, Bookseries, Sort, Publish, Bookinfor, Bookmember, Consume, Inoutrecord


class AuthorAdmin(admin.ModelAdmin):
  list_display = ('id', 'chn_name', 'for_name', 'area', 'birth', 'remark',)
#  list_filter = ('name',)

class BookseriesAdmin(admin.ModelAdmin):
  list_display = ('name',)

class SortAdmin(admin.ModelAdmin):
  list_display = ('name',)

class PublishAdmin(admin.ModelAdmin):
  list_display = ('id', 'name',)

class BookinforAdmin(admin.ModelAdmin):
  list_display = ('sn', 'book_name', 'book_set_name', 'series_name', 'publisher', 'size', 'edition', 'price', 'author_text', 'author_picture', 'translation', 'setset', 'hardcover', 'sortname', 'pinyin', 'per_amount', 'book_status', 'book_paper', 'position', 'language', 'true_price', 'book_link', 'isbn', 'remark1',)

class BookmemberAdmin(admin.ModelAdmin):
  list_display = ('phone', 'name', 'account', 'mail', 'begin','expir', 'card', 'remain', 'handler', 'remark',)

class ConsumeAdmin(admin.ModelAdmin):
  list_display = ('phone', 'consumetime', 'money', 'handler', 'over', 'deposit', 'sort', 'remark',)

class InoutrecordAdmin(admin.ModelAdmin):
  list_display = ('phone', 'outtime', 'intime', 'name', 'sn', 'handlerout', 'handlerin', 'remark',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Bookseries, BookseriesAdmin)
admin.site.register(Sort, SortAdmin)
admin.site.register(Publish, PublishAdmin)
admin.site.register(Bookinfor, BookinforAdmin)
admin.site.register(Bookmember, BookmemberAdmin)
admin.site.register(Consume, ConsumeAdmin)
admin.site.register(Inoutrecord, InoutrecordAdmin)



