from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.sales'
    verbose_name = 'Ventas'
    icon = 'icon-delivery-fast'