from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    cost = models.IntegerField()

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

    def __str__(self):
        return f'Order items : {self.menu}'

    def save(self, *args,  **kwargs):
        self.cost = self.menu.price * self.qty
        super().save(*args, **kwargs)


class Table(models.Model):
    tb_number = models.IntegerField()

    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'

    def __str__(self):
        return f'Table : {self.tb_number}'



class Order(models.Model):
    order_from = models.OneToOneField(Table, on_delete=models.PROTECT)
    qty = models.IntegerField(default=1)
    order_item = models.ManyToManyField('OrderItem')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order : '

    def save(self, *args, **kwargs):
        if self.id:
            self.qty = sum([i.qty for i in self.order_item.all()])
        super(Order, self).save()






# Create your models here.
