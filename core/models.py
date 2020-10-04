# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CargoEmpleado(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    nombre_cargo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargo_empleado'


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    primer_ape = models.CharField(max_length=40, blank=True, null=True)
    segundo_ape = models.CharField(max_length=40, blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nac = models.DateField(blank=True, null=True)
    correo = models.CharField(max_length=30)
    frecuente = models.BooleanField()
    id_comuna = models.IntegerField(blank=True, null=True)
    id_region = models.IntegerField(blank=True, null=True)
    id_nacionalidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'


class Departamento(models.Model):
    id_departamento = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    m_cuadrados = models.CharField(max_length=20, blank=True, null=True)
    banios = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=500)
    cantidad_habitacion = models.IntegerField(blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)
    id_region = models.IntegerField(blank=True, null=True)
    id_comuna = models.IntegerField(blank=True, null=True)
    id_inventario = models.IntegerField(blank=True, null=True)
    id_funcionario = models.IntegerField(blank=True, null=True)
    id_servicios_extra = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    rut_func = models.CharField(max_length=10, blank=True, null=True)
    nombre_func = models.CharField(max_length=20, blank=True, null=True)
    primer_ape_func = models.CharField(max_length=30, blank=True, null=True)
    segundo_ape_func = models.CharField(max_length=30, blank=True, null=True)
    fecha_nac_func = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=60, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)
    sueldo = models.IntegerField()
    fecha_contra = models.DateField(blank=True, null=True)
    id_cargo = models.IntegerField(blank=True, null=True)
    id_nacionalidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class EstadoDepartamento(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_departamento'


class EstadoInmueble(models.Model):
    id_estado_mueble = models.IntegerField(primary_key=True)
    nombre_estado = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_inmueble'


class EstadoReserva(models.Model):
    id_estado_reserva = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_reserva'


class FacturaBoleta(models.Model):
    id_boleta_factura = models.IntegerField(primary_key=True)
    num_factura_boleta = models.IntegerField(blank=True, null=True)
    foto = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura_boleta'


class Inventario(models.Model):
    id_inventario = models.IntegerField(primary_key=True)
    nombre_mueble = models.CharField(max_length=40, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    id_zona_inmueble = models.IntegerField(blank=True, null=True)
    id_departamento = models.IntegerField(blank=True, null=True)
    id_estado_mueble = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario'


class MantencionDepartamento(models.Model):
    id_mantenimiento = models.IntegerField(primary_key=True)
    descripcion_mante = models.CharField(max_length=40, blank=True, null=True)
    costo = models.IntegerField(blank=True, null=True)
    id_departamento = models.IntegerField(blank=True, null=True)
    id_boleta_factura = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mantencion_departamento'


class Nacion(models.Model):
    id_nacionalidad = models.IntegerField(primary_key=True)
    nombre_nacion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nacion'


class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region'


class ReservaDepartamento(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    fecha_rev_ini = models.DateField(blank=True, null=True)
    fecha_rev_fin = models.DateField(blank=True, null=True)
    total_rev = models.IntegerField(blank=True, null=True)
    pago_rev = models.IntegerField(blank=True, null=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    id_estado_reserva = models.IntegerField(blank=True, null=True)
    id_pago = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva_departamento'


class ServiciosBasicos(models.Model):
    id_servicios_basicos = models.IntegerField(primary_key=True)
    descripcion_servicio = models.CharField(max_length=40, blank=True, null=True)
    total_pago_serv = models.IntegerField(blank=True, null=True)
    id_boleta_factura = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios_basicos'


class ServiciosExtra(models.Model):
    id_servicios_extra = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios_extra'


class ZonaMueble(models.Model):
    id_zona_inmueble = models.IntegerField(primary_key=True)
    nombre_zona = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zona_mueble'
