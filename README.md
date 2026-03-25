# 🧮 AdCalSci — Advanced Calculator Scientific

**Calculadora científica web desarrollada con Flask y SQLite**  
*Evolución desde CLI básica · Arquitectura modular · Persistencia real · Autenticación de usuarios*

---

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-Persistencia-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://docs.python.org/3/library/sqlite3.html)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)](https://flask-sqlalchemy.palletsprojects.com)
[![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-Estilos-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/es/docs/Web/CSS)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](https://github.com/kindred-98/IA_PROG_CalculadoC.py)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

---

## 📌 Índice

- [Descripción](#-descripción)
- [Evolución del proyecto](#-evolución-del-proyecto)
- [Características](#-características)
- [Arquitectura](#-arquitectura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#️-uso)
- [Conceptos backend aplicados](#-conceptos-backend-aplicados)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Tecnologías](#-tecnologías)
- [Changelog](#-changelog)
- [Autor](#-autor)
- [Licencia](#-licencia)

---

## 📖 Descripción

**AdCalSci** es una calculadora científica web con historial persistente, autenticación de usuarios y arquitectura backend modular. Cada usuario tiene su propia sesión y su propio historial de operaciones almacenado en SQLite.

El proyecto fue construido con foco en:

- 🏗️ **Arquitectura modular** — separación clara entre rutas, modelos y lógica matemática
- 🔐 **Autenticación real** — registro, login, logout y hash de contraseñas
- 🗄️ **Persistencia SQLite** — historial por usuario con relaciones ForeignKey
- 📐 **Separación de responsabilidades** — cada módulo tiene un único propósito
- 🌐 **Interfaz web** — frontend en HTML5 y CSS3 servido por Flask

---

## 🔄 Evolución del proyecto

Este proyecto nació como una calculadora básica de consola en Python puro y evolucionó progresivamente hasta convertirse en una aplicación web completa:

| Etapa | Descripción |
|---|---|
| **v0.1 — CLI básica** | Función `calcular()` con suma, resta, multiplicación y división. Validación de división por cero. Ejecutable desde terminal. |
| **v0.2 — Web + historial en memoria** | Migración a Flask. Interfaz HTML con historial de operaciones almacenado en sesión (sin persistencia). |
| **v0.3 — Persistencia SQLite** | Incorporación de Flask-SQLAlchemy. Historial guardado en base de datos real. Borrado completo del historial. |
| **v1.0 — Autenticación de usuarios** | Registro y login con hash de contraseñas. Historial privado por usuario. Rutas protegidas. Logout. |

---

## 🚀 Características

| Funcionalidad | Descripción | Estado |
|---|---|---|
| Operaciones básicas | Suma, resta, multiplicación, división | ✅ |
| Operaciones científicas | Funciones matemáticas avanzadas | ✅ |
| Formateo de resultados | Máximo 10 decimales | ✅ |
| Historial persistente | Almacenado en SQLite por usuario | ✅ |
| Autenticación | Registro, login y logout | ✅ |
| Hash de contraseñas | Almacenamiento seguro de credenciales | ✅ |
| Historial privado | Cada usuario ve solo sus operaciones | ✅ |
| Borrado de historial | El usuario borra solo su propio historial | ✅ |
| Arquitectura modular | Rutas, modelos y lógica separados | ✅ |

---

## 🧠 Arquitectura del proyecto

```
┌─────────────────────────────────────────────────────────────────┐
│                          AdCalSci                               │
│                                                                 │
│  ┌──────────────────┐        ┌─────────────────────────────┐   │
│  │   templates/     │        │          app/               │   │
│  │                  │◄──────►│                             │   │
│  │  index.html      │        │  routes.py   → lógica web   │   │
│  │                  │        │  models.py   → ORM/BD       │   │
│  └──────────────────┘        │  calculator.py → matemática │   │
│                              │  __init__.py → init Flask   │   │
│  ┌──────────────────┐        └─────────────────────────────┘   │
│  │   static/        │                     │                    │
│  │                  │                     ▼                    │
│  │  style.css       │        ┌─────────────────────────────┐   │
│  │                  │        │         SQLite              │   │
│  └──────────────────┘        │                             │   │
│                              │  Usuario  ──┐               │   │
│                              │  Operacion ◄┘ (ForeignKey)  │   │
│                              └─────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 Instalación

### Requisitos previos

- Python 3.12 o superior
- pip

### Pasos

**1. Clonar el repositorio:**

```bash
git clone https://github.com/kindred-98/IA_PROG_CalculadoC.py.git
cd IA_PROG_CalculadoC.py/IA-pro-edu-main
```

**2. Crear entorno virtual:**

```bash
python -m venv .venv
```

**3. Activar entorno:**

```bash
# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

**4. Instalar dependencias:**

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

### Iniciar la aplicación

```bash
python run.py
```

La aplicación estará disponible en `http://127.0.0.1:5000`

### Flujo de usuario

```
1. Registrarse con usuario y contraseña
2. Iniciar sesión
3. Realizar operaciones matemáticas
4. Consultar historial personal
5. Borrar historial (solo el propio)
6. Cerrar sesión
```

---

## 🔧 Conceptos backend aplicados

| Concepto | Implementación |
|---|---|
| Separación de responsabilidades | Módulos independientes para rutas, modelos y lógica matemática |
| Blueprint | Organización modular de rutas en Flask |
| Modelos relacionales | `ForeignKey` entre `Usuario` y `Operacion` |
| ORM | `db.session.add()` y `db.session.commit()` con Flask-SQLAlchemy |
| Hash de contraseñas | Almacenamiento seguro sin texto plano |
| Sesiones | Control de acceso con `session` de Flask |
| Rutas protegidas | Redirección a login si no hay sesión activa |

---

## 📂 Estructura del proyecto

```
IA-pro-edu-main/
│
├── run.py                        # Punto de entrada
│
├── app/
│   ├── __init__.py               # Inicialización de Flask y base de datos
│   ├── models.py                 # Modelos Usuario y Operacion
│   ├── routes.py                 # Rutas principales y lógica de guardado
│   └── calculator.py             # Lógica matemática separada
│
├── templates/
│   └── index.html                # Interfaz web principal
│
├── static/
│   └── style.css                 # Estilos de la interfaz
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠 Tecnologías

| Tecnología | Uso |
|---|---|
| [Python 3.12+](https://python.org) | Lenguaje principal |
| [Flask](https://flask.palletsprojects.com) | Framework web |
| [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com) | ORM para base de datos |
| [SQLite](https://docs.python.org/3/library/sqlite3.html) | Base de datos embebida |
| [HTML5](https://developer.mozilla.org/es/docs/Web/HTML) | Interfaz de usuario |
| [CSS3](https://developer.mozilla.org/es/docs/Web/CSS) | Estilos visuales |

---

## 📋 Changelog

### v1.0.0 — 2026-02-24

- ✅ Autenticación completa: registro, login y logout
- ✅ Hash de contraseñas para almacenamiento seguro
- ✅ Verificación de duplicados en registro
- ✅ Historial privado por usuario via ForeignKey
- ✅ Rutas protegidas — redirección si no hay sesión activa
- ✅ Borrado de historial limitado al usuario autenticado

### v0.3.0

- ✅ Migración a Flask-SQLAlchemy
- ✅ Persistencia real del historial en SQLite
- ✅ Borrado completo del historial

### v0.2.0

- ✅ Migración a Flask con interfaz web HTML/CSS
- ✅ Historial de operaciones en sesión

### v0.1.0

- ✅ Calculadora básica en consola: suma, resta, multiplicación, división
- ✅ Validación de división por cero
- ✅ Función `calcular()` documentada con docstring

---

## 👨‍💻 Autor

**A.D.E.V.**

*Proyecto educativo del Módulo 2 — Estrategias de Generación de Código con IA · Dicampus*  
*Enfocado en arquitectura modular, persistencia de datos y evolución progresiva de software.*

[![GitHub](https://img.shields.io/badge/GitHub-kindred--98-181717?style=for-the-badge&logo=github)](https://github.com/kindred-98)

---

## 📜 Licencia

Este proyecto está distribuido bajo la licencia **MIT**.

---

*Hecho con 🧮 Python, Flask y arquitectura progresiva*

⭐ Si este proyecto te resulta útil, considera dejarle una estrella en GitHub