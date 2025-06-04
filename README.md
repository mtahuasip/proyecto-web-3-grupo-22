### Sistema de Préstamos de Biblioteca

## Tablas:

Libro, Préstamo, Socio, Multa (opcional).

## Funcionalidades:

Fechas de devolución, historial de préstamos, renovación.

---

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
