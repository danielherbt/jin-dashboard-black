# Generated by Django 4.0.1 on 2022-08-11 18:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(help_text='Descripción', max_length=100, unique=True, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, help_text='Código Único', max_length=50, null=True, unique=True, verbose_name='Código')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('dni', models.CharField(help_text='Número de Identificación', max_length=13, unique=True, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]{10,13}', 'Letras o números solamente')], verbose_name='Identificación')),
                ('name', models.CharField(help_text='Nombre o Razón Social', max_length=100, verbose_name='Nombre')),
                ('lastname', models.CharField(blank=True, help_text='Apellido o Nombre Comercial', max_length=100, null=True, verbose_name='Segundo Nombre')),
                ('birth', models.DateField(blank=True, help_text='Fecha de Cumpleaños', null=True, verbose_name='Natalicio')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo Electrónico')),
                ('photo', models.ImageField(blank=True, help_text='Foto o Imagen en formato png', max_length=255, null=True, upload_to='img', verbose_name='Imagen')),
                ('comment', models.TextField(blank=True, default=None, help_text='Información Adicional', null=True, verbose_name='Observaciones')),
                ('agentret', models.BooleanField(help_text='Si es agente de Retención', verbose_name='Retención')),
                ('artisan', models.BooleanField(help_text='Si es artesano', verbose_name='Artesano')),
                ('micro', models.BooleanField(help_text='Si es microempresa', verbose_name='Microempresa')),
                ('electronic', models.BooleanField(help_text='Si factura electrónicamente', verbose_name='Electrónica')),
                ('account', models.BooleanField(help_text='Si es Obligado a llevar contabilidad', verbose_name='Contabilidad')),
                ('agent', models.CharField(max_length=255, verbose_name='Representante')),
                ('agentdni', models.CharField(help_text='Cédula del Representante Legal', max_length=10, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]{10,13}', 'Letras o números solamente')], verbose_name='Dni Representante')),
                ('accountant', models.CharField(max_length=255, verbose_name='Contador')),
                ('accountantdni', models.CharField(help_text='Ruc del Contador', max_length=13, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]{10,13}', 'Letras o números solamente')], verbose_name='Dni Contador')),
                ('genre', models.ForeignKey(help_text='Tipo o Género', on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='base.genre', verbose_name='Género')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ConnectDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(help_text='Descripción', max_length=100, unique=True, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, help_text='Código Único', max_length=50, null=True, unique=True, verbose_name='Código')),
                ('dbms', models.CharField(blank=True, help_text='Motor de Base de Datos', max_length=50, null=True, verbose_name='DBMS')),
                ('port', models.CharField(blank=True, help_text='Puerto de la Base de Datos', max_length=7, null=True, verbose_name='Puerto')),
                ('user', models.CharField(blank=True, help_text='Usuario de la Base de Datos', max_length=50, null=True, verbose_name='Usuario')),
                ('passw', models.CharField(blank=True, help_text='Clave de la Base de Datos', max_length=20, null=True, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'Conexion',
                'verbose_name_plural': 'Conexiones',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(help_text='Descripción', max_length=100, unique=True, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, help_text='Código Único', max_length=50, null=True, unique=True, verbose_name='Código')),
            ],
            options={
                'verbose_name': 'País',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(help_text='Descripción', max_length=100, unique=True, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, help_text='Código Único', max_length=50, null=True, unique=True, verbose_name='Código')),
                ('city', models.ForeignKey(help_text='En que ciudad esta ubicada', on_delete=django.db.models.deletion.RESTRICT, to='manage.city', verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Parroquia',
                'verbose_name_plural': 'Parroquias',
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(help_text='Descripción', max_length=100, unique=True, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, help_text='Código Único', max_length=50, null=True, unique=True, verbose_name='Código')),
            ],
            options={
                'verbose_name': 'Modulo',
                'verbose_name_plural': 'Modulos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UsersDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(help_text='Descripción', max_length=100, unique=True, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, help_text='Código Único', max_length=50, null=True, unique=True, verbose_name='Código')),
                ('company', models.ForeignKey(help_text='Compania a la que pertenece', on_delete=django.db.models.deletion.RESTRICT, to='manage.company', verbose_name='Compania')),
                ('connect', models.ForeignKey(help_text='Perfil de Conexion', on_delete=django.db.models.deletion.RESTRICT, to='manage.connectdb', verbose_name='Conexion')),
                ('user', models.ForeignKey(help_text='Usuario del Sistema', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Usuario BD',
                'verbose_name_plural': 'Usuarios BD',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subsidiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('dni', models.CharField(help_text='Número de Identificación', max_length=13, unique=True, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]{10,13}', 'Letras o números solamente')], verbose_name='Identificación')),
                ('name', models.CharField(help_text='Nombre o Razón Social', max_length=100, verbose_name='Nombre')),
                ('lastname', models.CharField(blank=True, help_text='Apellido o Nombre Comercial', max_length=100, null=True, verbose_name='Segundo Nombre')),
                ('birth', models.DateField(blank=True, help_text='Fecha de Cumpleaños', null=True, verbose_name='Natalicio')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo Electrónico')),
                ('photo', models.ImageField(blank=True, help_text='Foto o Imagen en formato png', max_length=255, null=True, upload_to='img', verbose_name='Imagen')),
                ('comment', models.TextField(blank=True, default=None, help_text='Información Adicional', null=True, verbose_name='Observaciones')),
                ('matrix', models.BooleanField(help_text='Si es la matriz', verbose_name='Matriz')),
                ('serie', models.CharField(blank=True, help_text='Número de Serie SRI', max_length=7, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{3}-[0-9]{3}', 'Debe tener el formato "###-###"')], verbose_name='Serie')),
                ('company', models.ForeignKey(help_text='Compania a la que pertenece', on_delete=django.db.models.deletion.RESTRICT, to='manage.company', verbose_name='Compania')),
                ('genre', models.ForeignKey(help_text='Tipo o Género', on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='base.genre', verbose_name='Género')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SubDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(help_text='Descripción', max_length=100, unique=True, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, help_text='Código Único', max_length=50, null=True, unique=True, verbose_name='Código')),
                ('district', models.ForeignKey(help_text='En que parroquia esta ubicada', on_delete=django.db.models.deletion.RESTRICT, to='manage.district', verbose_name='Parroquia')),
            ],
            options={
                'verbose_name': 'Subparroquia',
                'verbose_name_plural': 'Subparroquias',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(help_text='Descripción', max_length=100, unique=True, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, help_text='Código Único', max_length=50, null=True, unique=True, verbose_name='Código')),
                ('country', models.ForeignKey(help_text='En que país esta ubicado', on_delete=django.db.models.deletion.RESTRICT, to='manage.country', verbose_name='País')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='HistoricalUsersDb',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(db_index=True, help_text='Descripción', max_length=100, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, db_index=True, help_text='Código Único', max_length=50, null=True, verbose_name='Código')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('company', models.ForeignKey(blank=True, db_constraint=False, help_text='Compania a la que pertenece', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='manage.company', verbose_name='Compania')),
                ('connect', models.ForeignKey(blank=True, db_constraint=False, help_text='Perfil de Conexion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='manage.connectdb', verbose_name='Conexion')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, help_text='Usuario del Sistema', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'historical Usuario BD',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSubsidiary',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('dni', models.CharField(db_index=True, help_text='Número de Identificación', max_length=13, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]{10,13}', 'Letras o números solamente')], verbose_name='Identificación')),
                ('name', models.CharField(help_text='Nombre o Razón Social', max_length=100, verbose_name='Nombre')),
                ('lastname', models.CharField(blank=True, help_text='Apellido o Nombre Comercial', max_length=100, null=True, verbose_name='Segundo Nombre')),
                ('birth', models.DateField(blank=True, help_text='Fecha de Cumpleaños', null=True, verbose_name='Natalicio')),
                ('email', models.EmailField(db_index=True, max_length=255, verbose_name='Correo Electrónico')),
                ('photo', models.TextField(blank=True, help_text='Foto o Imagen en formato png', max_length=255, null=True, verbose_name='Imagen')),
                ('comment', models.TextField(blank=True, default=None, help_text='Información Adicional', null=True, verbose_name='Observaciones')),
                ('matrix', models.BooleanField(help_text='Si es la matriz', verbose_name='Matriz')),
                ('serie', models.CharField(blank=True, help_text='Número de Serie SRI', max_length=7, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{3}-[0-9]{3}', 'Debe tener el formato "###-###"')], verbose_name='Serie')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('company', models.ForeignKey(blank=True, db_constraint=False, help_text='Compania a la que pertenece', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='manage.company', verbose_name='Compania')),
                ('genre', models.ForeignKey(blank=True, db_constraint=False, help_text='Tipo o Género', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.genre', verbose_name='Género')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Sucursal',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSubDistrict',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(db_index=True, help_text='Descripción', max_length=100, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, db_index=True, help_text='Código Único', max_length=50, null=True, verbose_name='Código')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('district', models.ForeignKey(blank=True, db_constraint=False, help_text='En que parroquia esta ubicada', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='manage.district', verbose_name='Parroquia')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Subparroquia',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalState',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(db_index=True, help_text='Descripción', max_length=100, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, db_index=True, help_text='Código Único', max_length=50, null=True, verbose_name='Código')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('country', models.ForeignKey(blank=True, db_constraint=False, help_text='En que país esta ubicado', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='manage.country', verbose_name='País')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Provincia',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalModules',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(db_index=True, help_text='Descripción', max_length=100, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, db_index=True, help_text='Código Único', max_length=50, null=True, verbose_name='Código')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modulo',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDistrict',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(db_index=True, help_text='Descripción', max_length=100, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, db_index=True, help_text='Código Único', max_length=50, null=True, verbose_name='Código')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('city', models.ForeignKey(blank=True, db_constraint=False, help_text='En que ciudad esta ubicada', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='manage.city', verbose_name='Ciudad')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Parroquia',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCountry',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(db_index=True, help_text='Descripción', max_length=100, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, db_index=True, help_text='Código Único', max_length=50, null=True, verbose_name='Código')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical País',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalConnectDb',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(db_index=True, help_text='Descripción', max_length=100, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, db_index=True, help_text='Código Único', max_length=50, null=True, verbose_name='Código')),
                ('dbms', models.CharField(blank=True, help_text='Motor de Base de Datos', max_length=50, null=True, verbose_name='DBMS')),
                ('port', models.CharField(blank=True, help_text='Puerto de la Base de Datos', max_length=7, null=True, verbose_name='Puerto')),
                ('user', models.CharField(blank=True, help_text='Usuario de la Base de Datos', max_length=50, null=True, verbose_name='Usuario')),
                ('passw', models.CharField(blank=True, help_text='Clave de la Base de Datos', max_length=20, null=True, verbose_name='Password')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Conexion',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCompany',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('dni', models.CharField(db_index=True, help_text='Número de Identificación', max_length=13, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]{10,13}', 'Letras o números solamente')], verbose_name='Identificación')),
                ('name', models.CharField(help_text='Nombre o Razón Social', max_length=100, verbose_name='Nombre')),
                ('lastname', models.CharField(blank=True, help_text='Apellido o Nombre Comercial', max_length=100, null=True, verbose_name='Segundo Nombre')),
                ('birth', models.DateField(blank=True, help_text='Fecha de Cumpleaños', null=True, verbose_name='Natalicio')),
                ('email', models.EmailField(db_index=True, max_length=255, verbose_name='Correo Electrónico')),
                ('photo', models.TextField(blank=True, help_text='Foto o Imagen en formato png', max_length=255, null=True, verbose_name='Imagen')),
                ('comment', models.TextField(blank=True, default=None, help_text='Información Adicional', null=True, verbose_name='Observaciones')),
                ('agentret', models.BooleanField(help_text='Si es agente de Retención', verbose_name='Retención')),
                ('artisan', models.BooleanField(help_text='Si es artesano', verbose_name='Artesano')),
                ('micro', models.BooleanField(help_text='Si es microempresa', verbose_name='Microempresa')),
                ('electronic', models.BooleanField(help_text='Si factura electrónicamente', verbose_name='Electrónica')),
                ('account', models.BooleanField(help_text='Si es Obligado a llevar contabilidad', verbose_name='Contabilidad')),
                ('agent', models.CharField(max_length=255, verbose_name='Representante')),
                ('agentdni', models.CharField(help_text='Cédula del Representante Legal', max_length=10, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]{10,13}', 'Letras o números solamente')], verbose_name='Dni Representante')),
                ('accountant', models.CharField(max_length=255, verbose_name='Contador')),
                ('accountantdni', models.CharField(help_text='Ruc del Contador', max_length=13, validators=[django.core.validators.RegexValidator('^[A-Za-z0-9]{10,13}', 'Letras o números solamente')], verbose_name='Dni Contador')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('genre', models.ForeignKey(blank=True, db_constraint=False, help_text='Tipo o Género', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.genre', verbose_name='Género')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Empresa',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCity',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.BooleanField(default=1, verbose_name='Activo')),
                ('created', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Creación', verbose_name='Creado')),
                ('updated', models.DateTimeField(blank=True, editable=False, help_text='Fecha de Modificación', verbose_name='Modificado')),
                ('name', models.CharField(db_index=True, help_text='Descripción', max_length=100, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, db_index=True, help_text='Código Único', max_length=50, null=True, verbose_name='Código')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(blank=True, db_constraint=False, help_text='En que provincia esta ubicada', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='manage.state', verbose_name='Provincia')),
            ],
            options={
                'verbose_name': 'historical Ciudad',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(help_text='En que provincia esta ubicada', on_delete=django.db.models.deletion.RESTRICT, to='manage.state', verbose_name='Provincia'),
        ),
    ]
