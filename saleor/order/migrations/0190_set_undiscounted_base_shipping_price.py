# Generated by Django 3.2.25 on 2024-07-25 08:28

from django.apps import apps as registry
from django.db import migrations
from django.db.models.signals import post_migrate

from .tasks.saleor3_19 import set_udniscounted_base_shipping_price_on_orders_task


def set_udniscounted_base_shipping_price(apps, _schema_editor):
    def on_migrations_complete(sender=None, **kwargs):
        set_udniscounted_base_shipping_price_on_orders_task.delay()

    sender = registry.get_app_config("account")
    post_migrate.connect(on_migrations_complete, weak=False, sender=sender)


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0189_set_undiscounted_base_shipping_price"),
    ]

    operations = [
        migrations.RunPython(
            set_udniscounted_base_shipping_price,
            reverse_code=migrations.RunPython.noop,
        )
    ]