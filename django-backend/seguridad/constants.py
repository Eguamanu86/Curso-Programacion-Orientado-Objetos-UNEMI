from django.db import models
from django.utils.translation import gettext_lazy as _

class Gender(models.TextChoices):
    MALE = "Male", _("Masculino")
    FEMALE = "Female", _("Femenino")
    OTHER = "Other", _("Otro")

class Sex(models.TextChoices):
    MALE = "Men", _("Hombre")
    FEMALE = "Woman", _("Mujer")
    OTHER = "Other", _("Otro")

class CategoryModule(models.TextChoices):
    MAINTENANCE = "Maintenance", _("Mantenimientos")
    DOCUMENTS = "Documents", _("Documentos")
    PROCESSES = "Processes", _("Procesos")
    REPORTS = "Resports", _("Informes")
    SECURITY = "Security", _("Seguridad")
    OTHER = "Other", _("Otro")

class TypeModule(models.TextChoices):
    MENU = "Menu", _("Menu")
    SUBMENU = "submenu", _("submenu")
    LIST_RESOURCE = "List Resource", _("Listar Recurso")
    ACTION_RESOURCE = "Action Resource", _("Accion Recurso")
    OTHER = "Other", _("Otro")

MESES  = (
    (1,"ENERO"),
    (2,"FEBRERO"),
    (3,"MARZO"),
    (4,"ABRIL"),
    (5,"MAYO"),
    (6,"JUNIO"),
    (7,"JULIO"),
    (8,"AGOSTO"),
    (9,"SEPTIEMBRE"),
    (10,"OCTUBRE"),
    (11,"NOVIEMBRE"),
    (12,"DICIEMBRE")
)

SYSTEM_LOGO = 'fas fa-globe-americas fa-2x'
SYSTEM_NAME = 'Global | Registry '
SISTEMA_AUTOR = 'Ing. Ernesto Guamán U.'
SYSTEM_WEB = 'www.globalregistry.com'
