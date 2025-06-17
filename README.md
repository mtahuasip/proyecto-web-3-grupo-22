### Sistema de Préstamos de Biblioteca

## Descripción del Sistema

El Sistema de Préstamos de Biblioteca es una aplicación web desarrollada con el framework **Django** que permite gestionar de manera eficiente el préstamo y devolución de libros en una biblioteca académica o institucional. Su propósito principal es facilitar la administración del inventario bibliográfico, el control de socios y el seguimiento de los préstamos realizados, mejorando la organización interna y el acceso a los recursos.

## Objetivos del Proyecto

El objetivo principal del sistema es desarrollar una plataforma basada en Django que optimice la gestión de préstamos y devoluciones de libros, mejorando la administración del inventario bibliográfico y el control de usuarios.

**Objetivos específicos:**

- Automatizar el proceso de préstamo y devolución de libros.
- Facilitar la administración de socios y usuarios.
- Implementar un sistema de control de disponibilidad de libros.
- Registrar y gestionar el historial de préstamos.
- Desarrollar un módulo de multas basado en retrasos en devoluciones.
- Crear una interfaz intuitiva y adaptable a distintos roles de usuario.
- Garantizar la seguridad y privacidad de los datos.
- Integrar reportes y estadísticas sobre el uso del sistema.

## Funcionalidades

Entre sus principales funcionalidades se encuentran:

- Registro y gestión de libros, incluyendo su disponibilidad.
- Administración de socios, permitiendo la gestión de usuarios habilitados para realizar préstamos.
- Control de préstamos y devoluciones, con registro automático de fechas.
- Renovación de préstamos dentro de los plazos permitidos.
- Historial de préstamos por socio, permitiendo consultar movimientos anteriores.
- Módulo de multas, calculadas en base a retrasos en la devolución de libros.


## Requisitos Previos

- Python 3.8 o superior instalado
- pip (gestor de paquetes de Python)
- Git (opcional, si clonas el repositorio)

---

## Instrucciones para configurar el entorno y ejecutar el proyecto

### 1. Clonar el repositorio (opcional)

```bash
git clone https://github.com/mtahuasip/proyecto-web-iii-grupo-20-django.git
cd proyecto-web-iii-grupo-20-django
```

### 2. Crear y activar el entorno virtual

En sistemas Unix/Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

En Windows (PowerShell):

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1

```

### 3. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 6. Ejecutar las migraciones iniciales

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```
