from django.contrib import admin
from django.contrib import messages
from api.base.models import Genre
from api.manage.models import City, Company, Country, District, State, SubDistrict, Subsidiary, Modules, ConnectDb, UsersDb

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(District)
admin.site.register(SubDistrict)
admin.site.register(Company)
admin.site.register(Subsidiary)
admin.site.register(Modules)

class ConnectDbAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'dbms', 'port','user')
    search_fields = ('name', 'code')

admin.site.register(ConnectDb,ConnectDbAdmin)

admin.site.register(Genre)


class UserDbAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información para la Conexión del Usuario', {
            "fields": ('user','connect','company','name','code'
                
            ),
        }),
    )
    
    list_display = ('pk','code', 'name','user', 'connect','company')
    list_display_links = ('pk','code', 'connect')
    search_fields = ('name', 'code', 'connect__name','company__name','user__name')
    date_hierarchy = 'created'
    prepopulated_fields = {"code": ('user','connect','company','name')}
    
    # Para agregar acciones a los seleccionados
    # https://coffeebytes.dev/el-django-admin-panel-y-su-personalizacion/
    # def rate_five_stars(modeladmin, request, queryset):
    #     queryset.update(rating=5.0)
    #     messages.success(request, "Se calificó con 5 estrellas")
    # admin.site.add_action(rate_five_stars, "Calificar con 5 estrellas")
    ### Icono para el modulo
    # https://materializecss.com/icons.html
    #icon_name = 'recent_actors'

    ### Desplegar atributos de tabla relacionada
    #def Codigo(self, obj):
    #    return obj.user.username +'/' + obj.connect.name +'/' + obj.name    
 
admin.site.register(UsersDb, UserDbAdmin)
