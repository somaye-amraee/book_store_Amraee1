# Generated by Django 3.2.6 on 2021-08-31 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasketDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_type', models.CharField(choices=[('C', 'مقداری'), ('P', 'درصدی'), ('S', 'امتیازی')], default='C', max_length=5)),
                ('cash_discount', models.PositiveIntegerField(default=0, verbose_name='مقدار تخفیف نقدی')),
                ('percent_discount', models.PositiveIntegerField(default=0, verbose_name='مقدار تخفیف درصدی')),
                ('star_discount', models.PositiveIntegerField(default=0, verbose_name='تخفیف امتیازی')),
                ('validate_date', models.DateTimeField(verbose_name='تاریخ اعمال کد تخفیف')),
                ('expire_date', models.DateTimeField(verbose_name='تاریخ اعتبار کد تخفیف')),
                ('active', models.BooleanField(default=False, verbose_name='وضعیت تخفیف')),
                ('code_discount', models.CharField(max_length=100, unique=True, verbose_name='کد تخفیف')),
            ],
            options={
                'verbose_name': 'تخفیف کددار',
                'verbose_name_plural': 'تخفیف های کددار',
            },
        ),
        migrations.CreateModel(
            name='ProductDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_type', models.CharField(choices=[('C', 'مقداری'), ('P', 'درصدی'), ('S', 'امتیازی')], default='C', max_length=5)),
                ('cash_discount', models.PositiveIntegerField(default=0, verbose_name='مقدار تخفیف نقدی')),
                ('percent_discount', models.PositiveIntegerField(default=0, verbose_name='مقدار تخفیف درصدی')),
                ('star_discount', models.PositiveIntegerField(default=0, verbose_name='تخفیف امتیازی')),
                ('validate_date', models.DateTimeField(verbose_name='تاریخ اعمال کد تخفیف')),
                ('expire_date', models.DateTimeField(verbose_name='تاریخ اعتبار کد تخفیف')),
                ('active', models.BooleanField(default=False, verbose_name='وضعیت تخفیف')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='نام تخفیف نقدی')),
                ('max_purchase', models.IntegerField(default=0, verbose_name='سقف تخفیف')),
            ],
            options={
                'verbose_name': 'تخفیف کتاب',
                'verbose_name_plural': 'تخفیف هایکتاب',
            },
        ),
    ]
