from django.db import models


class Person(models.Model):
    category = models.ForeignKey('Person_category', verbose_name='人员类别', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='姓名', max_length=200)
    remarks = models.CharField(verbose_name='备注', blank=True, max_length=500)

    class Meta:
        verbose_name = '就餐人员列表'
        verbose_name_plural = '就餐人员列表'

    def __str__(self):
        return self.name

class Person_category(models.Model):

    name = models.CharField('人员类别', max_length=100, unique=True) # unique为了防止重名
    remarks = models.CharField('备注', blank=True, max_length=500)
    breakfast_charge = models.IntegerField('早餐收费', default=2, blank=False)
    lunch_charge = models.IntegerField('午餐收费')
    dinner_charge = models.IntegerField('晚餐收费', default=0)


    class Meta:
        verbose_name = '人员类别'
        verbose_name_plural = '人员类别'

    def __str__(self):
        return self.name


class Week_menu(models.Model):
    """【待优化】本类作为 config 类来使用，存储菜单、参数等。
    如此使用，则系统部署时候，初始化步骤就必须包括如下 3 步
         - 超级管理员注册食堂管理员账号
         - 设置食堂管理员权限，限制对 Week_menu 的增减
         - 手动添加一个 Week_menu 对象
    """
    mon = models.TextField('星期一')
    tue = models.TextField('星期二')
    wed = models.TextField('星期三')
    thu = models.TextField('星期四')
    fri = models.TextField('星期五')
    sat = models.TextField('周六')
    sun = models.TextField('周日')
    # 为了让 views 可以直接获得 TextField 的 object
    menus = [mon, tue, wed, thu, fri, sat, sun]

    # 下面这些参数，将来应该另找地方专门存储
    breakfast_deadline = models.IntegerField('下次早餐订餐截止时间', default=16)
    lunch_deadline = models.IntegerField('当日午餐订餐截止时间', default=9)

    class Meta:
        verbose_name = '一周菜单'
        verbose_name_plural = '一周菜单'

    def __str__(self):
        return '点击更新一周菜单'


class Order(models.Model):
    MEAL_CATEGORY = (
        ('B', '早餐'),
        ('L', '午餐'),
        ('D', '晚餐'),
    )
    person = models.ForeignKey(Person)
    meal = models.CharField(max_length=1, choices=MEAL_CATEGORY)
    meal_date = models.DateTimeField('预定日期')
    order_date = models.DateTimeField('下单日期')


