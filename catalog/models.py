from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за единицу')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'Имя продукта: {self.name}  Категория:{self.category}   Цена: {self.price} рублей'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('price',)


class Contacts(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')

    def __str__(self):
        return f'{self.first_name} {self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    def __str__(self):
        return f'{self.name} {self.phone}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE, verbose_name='Наименование')
    version_number = models.IntegerField(verbose_name="номер версии")
    version_name = models.CharField(max_length=100, verbose_name="название версии")
    is_active = models.BooleanField(default=True, verbose_name='активная версия')

    def __str__(self):
        return f"{self.product}, {self.version_number}, {self.version_name}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
