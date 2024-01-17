from django.apps import AppConfig



class KasapartyConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "kasaparty"
    
    def ready(self):
        import kasaparty.models.signals  # Si tienes señales en tu aplicación