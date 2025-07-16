
# Hypixel API Tool by Al3xx_ux

Este proyecto es una aplicación de línea de comandos en Python que permite consultar datos de la API de Hypixel, como el leaderboard de wins, estadísticas de usuarios, número actual de jugadores y estadísticas de baneos de staff.

---

## Características

- Mostrar el **Top 10** de jugadores con más wins en Hypixel (todos los tiempos).
- Buscar estadísticas detalladas de un usuario por su nombre.
- Mostrar el número actual de jugadores en Hypixel.
- Consultar estadísticas de baneos realizados por staff y watchdog.
- Menú interactivo para una navegación sencilla.

---

## Requisitos

- Python 3.x
- Librería `requests`

---

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. Instala la dependencia necesaria:

```bash
pip install requests
```

3. Añade tu API Key de Hypixel en el archivo `main.py` (línea donde está `API_KEY = ""`):

```python
API_KEY = "tu_api_key_aqui"
```

---

## Uso

Ejecuta el script principal:

```bash
python main.py
```

Aparecerá un menú con las opciones disponibles, elige la que quieras ejecutando la opción correspondiente.

---

## Funciones

- **Win Leaderboard all time:** Muestra el top 10 de jugadores con más wins totales.
- **Search user stats:** Busca y muestra estadísticas detalladas de un jugador.
- **Current number of users:** Muestra el número actual de jugadores en Hypixel.
- **Staff bans:** Muestra estadísticas de baneos diarios y totales hechos por staff y watchdog.

---

## Notas

- Es necesaria una API Key válida de Hypixel para que el script funcione correctamente.
- La API de Mojang se usa para convertir nombres de usuario a UUID.
- El programa está diseñado para usarse en consola y requiere conexión a internet.

---
