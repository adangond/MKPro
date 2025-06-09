# MKPro

MKPro es una plataforma basada en Django diseñada para la gestión de productos, inventarios, ventas y usuarios con un enfoque en seguridad, eficiencia y diseño intuitivo. Está alineada con la identidad de la marca Mary Kay, adoptando una estética moderna con una paleta de colores rosa y blanco.

## Índice

- [Descripción General](#descripción-general)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación y Configuración](#instalación-y-configuración)
- [Gestión de Usuarios](#gestión-de-usuarios)
- [Gestión de Productos](#gestión-de-productos)
- [Pruebas Automatizadas](#pruebas-automatizadas)
- [Seguridad y Buenas Prácticas](#seguridad-y-buenas-prácticas)
- [Próximos Pasos](#próximos-pasos)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Descripción General

MKPro es un sistema modular que facilita la administración de productos y usuarios, asegurando un flujo de trabajo eficiente y seguro. Entre sus principales características se incluyen:

- **Gestión de Usuarios:** Registro, autenticación, edición de perfiles y administración de cuentas desde Django Admin.
- **Administración de Productos:** Creación, edición y gestión de inventarios con atributos personalizados.
- **Seguridad Avanzada:** Validaciones de formulario, protección CSRF y control de accesos mediante Django.
- **Interfaz Optimizada:** Uso de Tailwind CSS y crispy forms para una experiencia moderna y accesible.
- **Automatización y Pruebas:** Implementación de pruebas unitarias y de integración para asegurar estabilidad.

## Tecnologías Utilizadas

- **Backend:** Django 5.2.1
- **Frontend:** Tailwind CSS + crispy forms
- **Base de Datos:** SQLite (para desarrollo, soporta otras como PostgreSQL en producción)
- **Gestión y Administración:** Django Admin
- **Autenticación:** Sistema de usuarios basado en el modelo estándar de Django
- **Control de Código:** Git y GitHub

## Estructura del Proyecto

```bash
MKPro/
│── core/                  # Aplicación que maneja el homepage (index)
│   ├── __init__.py        # Inicialización de la app
│   ├── views.py           # Vista para el homepage
│   ├── urls.py            # Rutas específicas para la página principal
│   ├── templates/         # Plantillas del homepage
│── MKPro/                 # Configuración principal del proyecto
│   ├── __init__.py        # Inicialización de Django
│   ├── settings.py        # Configuración del proyecto Django
│   ├── urls.py            # Definición de rutas generales
│── users/                 # Aplicación para la gestión de usuarios
│   ├── __init__.py        # Inicialización de la app
│   ├── models.py          # Definición del modelo de usuarios
│   ├── views.py           # Vistas de la app users
│   ├── urls.py            # Rutas específicas para users
│   ├── templates/         # Plantillas de gestión de usuarios
│── products/              # Aplicación para la gestión de productos
│   ├── __init__.py        # Inicialización de la app
│   ├── models.py          # Definición del modelo de productos
│   ├── views.py           # Vistas de productos
│   ├── forms.py           # Formularios para productos
│   ├── urls.py            # Rutas específicas para products
│   ├── templates/         # Plantillas de gestión de productos
│── templates/             # Plantillas HTML globales
│── static/                # Archivos CSS, JS y multimedia
│── db.sqlite3             # Base de datos SQLite (en desarrollo)
│── requirements.txt       # Dependencias del proyecto
│── manage.py              # Script de administración de Django
```

## Instalación y Configuración

### 1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd MKPro
```

### 2. Crear y activar el entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate   # En Linux/macOS
.\.venv\Scripts\activate    # En Windows
```

### 3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones:

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor de desarrollo:

```bash
python manage.py runserver
```

Accede a la aplicación en `http://127.0.0.1:8000/`.

## Gestión de Usuarios

La aplicación **users** proporciona las siguientes funcionalidades:

- **Registro de Usuarios:** Formulario de inscripción validado con autenticación segura.
- **Inicio de Sesión:** Autenticación mediante credenciales con mensajes de error claros en español.
- **Edición de Perfil:** Actualización de datos personales con restricciones en campos sensibles.
- **Gestión de Contraseñas:** Cambio y restablecimiento de contraseña con protección CSRF.
- **Administración Interna:** Gestión completa de usuarios en Django Admin.

### Django Admin
Para acceder al panel administrativo, usa:

```bash
python manage.py createsuperuser
```

Luego inicia sesión en `/admin/`.

## Gestión de Productos

La aplicación **products** permite:

- **Creación y edición de productos:** Formularios con validaciones y categorización flexible.
- **Gestión de inventario:** Control de disponibilidad y estado del producto.
- **Redimensionamiento de imágenes:** Imágenes ajustadas automáticamente a 500x500 píxeles mediante PIL.

## Pruebas Automatizadas

Para ejecutar la batería de tests:

```bash
python manage.py test
```

Incluye validaciones sobre:

- Registro e inicio de sesión de usuarios.
- Actualización de perfiles y seguridad en autenticación.
- Creación y edición de productos.
- Gestión de contraseñas y validación de formularios.

## Seguridad y Buenas Prácticas

### **Protección CSRF**
Todos los formularios que requieren autenticación incluyen:

```html
{% csrf_token %}
```

### **Autoescape en Templates**
Django autoescapa todas las variables para evitar inyección de código malicioso (XSS).

### **Accesos Restringidos**
- Se usa `LoginRequiredMixin` en vistas sensibles para restringir el acceso a usuarios autenticados.
- La administración interna se gestiona desde Django Admin con permisos adecuados.

### **Validaciones en Formularios**
- Se implementan reglas estrictas para la creación de cuentas y gestión de datos sensibles.
- Se eliminan campos inseguros como `password` en formularios de edición de usuario.

## Próximos Pasos

El siguiente objetivo del proyecto es desarrollar los módulos de **compra y venta**, que incorporarán:

### **App de Compras:**
- Administración de entradas de inventario cuando se recibe el pedido de Mary Kay.
- Gestión de costos y proveedores.

### **App de Ventas:**
- Gestión de clientes.
- Procesamiento de pedidos y generación de facturas.
- Análisis de rendimiento comercial.

Estos módulos serán integrados con la estructura actual, manteniendo la coherencia y seguridad en toda la plataforma.

## Contribución

Si deseas colaborar en el proyecto, sigue estos pasos:

1. **Haz un fork del repositorio.**
2. **Crea una rama de desarrollo:**
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. **Realiza los cambios y prueba la funcionalidad.**
4. **Envía un Pull Request detallando tus contribuciones.**

## Licencia

Este proyecto se encuentra bajo la licencia **MIT**, permitiendo su uso, modificación y distribución libremente. 

---

**Estado Actual del Proyecto: En desarrollo 🔧**  
**Siguientes funcionalidades: Implementación de las aplicaciones de compras y ventas.**
