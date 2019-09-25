from django.contrib import admin
from .models import Author, Bookseries, Sort, Publish, Bookinfor, Bookmember, Consume, Inoutrecord


class AuthorAdmin(admin.ModelAdmin):
  list_display = ('chn_name', 'for_name', 'area', 'birth', 'remark',)
#  list_filter = ('name',)

class BookseriesAdmin(admin.ModelAdmin):
  list_display = ('name',)

class SortAdmin(admin.ModelAdmin):
  list_display = ('name',)

class PublishAdmin(admin.ModelAdmin):
  list_display = ('name',)

class BookinforAdmin(admin.ModelAdmin):
  list_display = ('book_name', 'book_set_name', 'series_name', 'publisher', 'size', 'edition', 'price', 'author_text', 'author_picture', 'translation', 'setset', 'hardcover', 'borrow_amount', 'pinyin', 'per_amount', 'set_amount', 'book_amount', 'borrow_amount', 'remain_amount', 'position', 'language', 'true_price', 'remark1', 'remark2',)

class BookmemberAdmin(admin.ModelAdmin):
  list_display = ('phone', 'name', 'account', 'mail', 'begin','expir', 'card', 'remain', 'handler', 'remark',)

class ConsumeAdmin(admin.ModelAdmin):
  list_display = ('phone', 'consumetime', 'money', 'handler', 'sort', 'remark',)

class InoutrecordAdmin(admin.ModelAdmin):
  list_display = ('phone', 'outtime', 'intime', 'name', 'zcbm', 'handlerout', 'handlerin', 'remark',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Bookseries, BookseriesAdmin)
admin.site.register(Sort, SortAdmin)
admin.site.register(Publish, PublishAdmin)
admin.site.register(Bookinfor, BookinforAdmin)
admin.site.register(Bookmember, BookmemberAdmin)
admin.site.register(Consume, ConsumeAdmin)
admin.site.register(Inoutrecord, InoutrecordAdmin)



