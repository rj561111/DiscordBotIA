# 🌱 Bot de Discord con IA - Clasificación de Plantas
Este proyecto consiste en un bot de Discord que utiliza un modelo de inteligencia artificial para identificar si una planta es **comestible o no comestible** a partir de una imagen.

## 🚀 Funcionalidades
* 📷 Analiza imágenes enviadas por el usuario
* 🤖 Clasifica plantas como:
  * Comestibles ✅
  * No comestibles ⚠️
* 📊 Muestra el nivel de confianza del modelo
* 🌿 Comando informativo sobre plantas
* 🎲 Ejemplos con imágenes aleatorias

## 🧠 Tecnologías utilizadas
* Python
* discord.py
* Modelo de IA (Teachable Machine)

## ⚙️ Instalación
1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```
2. Instala dependencias:
```bash
pip install discord.py
pip install tensorflow
```
3. Configura tu token de Discord:
   Reemplaza en el código:
```python
bot.run("TU_TOKEN_AQUI")
```
## 💬 Comandos del bot
| Comando      | Descripción                  |
| ------------ | ---------------------------- |
| `$hello`     | Saludo del bot               |
| `$heh`       | Repite "he"                  |
| `$verificar` | Analiza una imagen           |
| `$plantas`   | Información sobre plantas    |
| `$ejemplos`  | Muestra un ejemplo aleatorio |

## 📊 Ejemplo de uso
Sube una imagen y escribe:
```
$verificar
```
Respuesta:
```
🌱 Planta
🌿 Resultado: Plátano
📊 Confianza: 95.32%
```
## ⚠️ Advertencia
Este bot es solo con fines educativos.
No se debe utilizar como herramienta confiable para determinar si una planta es segura para el consumo.

