from django.db import models
import time

class Author(models.Model):
  chn_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='中文名称')
  for_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='外文名称')
  area = models.CharField(max_length=20, null=True, blank=True, verbose_name='国家/地区')
  birth = models.CharField(max_length=20, null=True, blank=True, verbose_name='出生年月')
  remark = models.CharField(max_length=100, null=True, blank=True, verbose_name='备注')


  def __str__(self):
    return self.chn_name


class Bookseries(models.Model):
  name = models.CharField(max_length=50, verbose_name='系列名称')

  def __str__(self):
    return self.name


class Sort(models.Model):
  name = models.CharField(max_length=50, verbose_name='类别')

  def __str__(self):
    return self.name


class Publish(models.Model):
  name = models.CharField(max_length=50, verbose_name='出版社')

  def __str__(self):
    return self.name


class Bookinfor(models.Model):
  sn = models.CharField(max_length=20, primary_key=True, default=time.strftime("%Y%m%d%H%M%S", time.localtime()), verbose_name='SN')
  book_name = models.CharField(max_length=30, verbose_name='书名')
  book_set_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='套装名称')
  series_name = models.ForeignKey(Bookseries, on_delete=models.CASCADE, null=True, blank=True, verbose_name='系列名称')
  publisher = models.ForeignKey(Publish, on_delete=models.CASCADE, null=True, blank=True, verbose_name='出版社')
  size = models.CharField(max_length=20, null=True, blank=True, verbose_name='大小')

  edition = models.CharField(max_length=30, null=True, blank=True, verbose_name='版次')
  price = models.CharField(max_length=10, null=True, blank=True, verbose_name='定价')
  author_text = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='author_text', verbose_name='著')
  author_picture = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='author_picture', verbose_name='绘')
  translation = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='translation', verbose_name='翻译')

  setset = models.CharField(max_length=10, null=True, blank=True, verbose_name='套装', choices=(('s','是'),('f','否')))
  hardcover = models.CharField(max_length=10, null=True, blank=True, verbose_name='装订', choices=(('jingz','精装'),('jianz','简装')))
  sortname = models.ForeignKey(Sort, on_delete=models.CASCADE, null=True, blank=True, verbose_name='类别')
  pinyin = models.CharField(max_length=10, null=True, blank=True, verbose_name='拼音')
  per_amount = models.CharField(max_length=20, null=True, blank=True, verbose_name='每套几本')
  book_status = models.CharField(max_length=10, null=True, blank=True, verbose_name='状态')
  book_paper = models.CharField(max_length=10, null=True, blank=True, verbose_name='纸张')

  position = models.CharField(max_length=20, null=True, blank=True, verbose_name='存放位置')
  language = models.CharField(max_length=20, null=True, blank=True, verbose_name='语言')
  true_price = models.CharField(max_length=20, null=True, blank=True, verbose_name='购买价格')
  book_link = models.CharField(max_length=50, null=True, blank=True, verbose_name='链接')
  isbn = models.CharField(max_length=20, null=True, blank=True, verbose_name='ISBN')
  remark1 = models.CharField(max_length=20, null=True, blank=True, verbose_name='备注1')

  def __str__(self):
    return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.sn, self.book_name, self.book_set_name, self.series_name, self.publisher, self.size, self.edition, self.price, self.author_text, self.author_picture, self.translation, self.setset, self.hardcover, self.sortname, self.pinyin, self.per_amount, self.book_status, self.book_paper, self.position, self.language, self.true_price, self.book_link, self.isbn, self.remark1)



class Bookmember(models.Model):
  phone = models.CharField(primary_key=True, max_length=20, verbose_name='电话')
  name = models.CharField(max_length=20, null=True, blank=True, verbose_name='姓名')
  account = models.CharField(max_length=20, null=True, blank=True, verbose_name='社交帐号')
  mail = models.CharField(max_length=20, null=True, blank=True, verbose_name='邮箱')
  begin = models.DateTimeField(null=True, blank=True, verbose_name='注册时间', auto_now_add = True)
  expir = models.DateTimeField(null=True, blank=True, verbose_name='过期时间', auto_now = False)
  card = models.CharField(max_length=20, null=True, blank=True, verbose_name='卡号')
  remain = models.CharField(max_length=20, null=True, blank=True, verbose_name='剩余金额', default="0")
  handler = models.CharField(max_length=10, null=True, blank=True, verbose_name='创建人')
  remark = models.CharField(max_length=100, null=True, blank=True, verbose_name='备注')


  def __str__(self):
    return self.phone
#    return '%s %s' % (self.phone, self.remain)



class Consume(models.Model):
  phone = models.CharField(max_length=20, verbose_name='电话')
  consumetime = models.DateTimeField(null=True, blank=True, verbose_name='消费时间', auto_now_add = True)
  money = models.CharField(max_length=20, null=True, blank=True, verbose_name='消费金额')
  handler = models.CharField(max_length=20, null=True, blank=True, verbose_name='操作人')
  sort = models.CharField(max_length=20, null=True, blank=True, verbose_name='类型', choices=(('cz','充值'),('xf','消费')))
  over = models.CharField(max_length=20, null=True, blank=True, verbose_name='余额')
  deposit = models.CharField(max_length=20, null=True, blank=True, verbose_name='押金')
  remark = models.CharField(max_length=100, null=True, blank=True, verbose_name='备注')


  def __str__(self):
    return self.phone



class Inoutrecord(models.Model):
  phone = models.CharField(max_length=20, verbose_name='电话')
  outtime = models.DateTimeField(null=True, blank=True, verbose_name='借出时间', auto_now_add = True)
  intime = models.DateTimeField(null=True, blank=True, verbose_name='归还时间')
  name = models.CharField(max_length=20, null=True, blank=True, verbose_name='书名')
  zcbm = models.CharField(max_length=20, null=True, blank=True, verbose_name='资产编码')
  handlerout = models.CharField(max_length=20, null=True, blank=True, verbose_name='操作人出')
  handlerin = models.CharField(max_length=20, null=True, blank=True, verbose_name='操作人还')
  remark = models.CharField(max_length=100, null=True, blank=True, verbose_name='备注')


  def __str__(self):
    return self.phone

