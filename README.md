# Reservas de Hotel en Python

Este proyecto es un sistema de gestión hotelera desarrollado en Python. La aplicación permite gestionar reservas, clientes, habitaciones y pagos de manera modular, utilizando una arquitectura bien definida para facilitar su mantenimiento y escalabilidad.

## Características principales

### Gestión de habitaciones:

Registro de habitaciones con detalles como tipo y precio.

Verificación de disponibilidad.

### Gestión de clientes:

Registro y almacenamiento de datos de clientes.

Consulta de información de clientes por ID.

### Gestión de reservas:

Creación de reservas con fechas de entrada y salida.

Cancelación de reservas por ID.

Verificación de conflictos de fechas para evitar duplicados.

### Procesamiento de pagos:

Simulación de pagos asincrónicos.

### Estructura modular:

Dividido en diferentes módulos: reservations.py, customers.py, rooms.py, y payments.py.
