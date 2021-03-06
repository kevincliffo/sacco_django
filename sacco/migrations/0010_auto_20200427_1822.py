# Generated by Django 3.0.5 on 2020-04-27 15:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0009_remove_financial_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(default='', max_length=100)),
                ('PaymentDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('TransactionDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('PaymentMonth', models.CharField(default='', max_length=100)),
                ('Amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('MemberNo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sacco.Member')),
            ],
        ),
        migrations.DeleteModel(
            name='Financial',
        ),
    ]
