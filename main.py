import discord
from discord.ext import commands
import os
import random

# IMPORTAR TU MODELO
from modelo import predecir_imagen

# ================================
# CONFIG
# ================================
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Crear carpeta imágenes
if not os.path.exists("images"):
    os.makedirs("images")

# ================================
# EVENTO
# ================================
@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

# ================================
# COMANDOS
# ================================
@bot.command()
async def hello(ctx):
    await ctx.send(f'👋 Hola! Soy {bot.user}')

@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)

# 🔍 ANALIZAR IMAGEN
@bot.command()
async def verificar(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre_archivo = archivo.filename
            ruta = f"./images/{nombre_archivo}"

            # Guardar imagen
            await archivo.save(ruta)

            # Usar IA
            clase, confianza = predecir_imagen(ruta)

            # Respuesta
            if "comestible" in clase.lower():
                mensaje = "🌱 Planta"
            else:
                mensaje = "🌱 Planta"

            await ctx.send(
                f"{mensaje}\n"
                f"🌿 Resultado: {clase}\n"
                f"📊 Confianza: {confianza*100:.2f}%"
            )
    else:
        await ctx.send("❌ No subiste ninguna imagen")

# 🌱 INFO
@bot.command()
async def plantas(ctx):
    await ctx.send(
        "🌱 Las plantas son seres vivos autótrofos (producen su propio alimento) que pertenecen al reino vegetal, caracterizados por no desplazarse, poseer células con celulosa y realizar la fotosíntesis. Utilizan luz solar, agua y dióxido de carbono para crecer, purificando el aire al liberar oxígeno. Sus partes principales son raíz, tallo, hojas, flores y frutos.\n\n"
        "Ejemplos:\n"
        "🍎 Manzano (comestible)\n"
        "🥬 Lechuga (comestible)\n"
        "☠️ Cicuta (venenosa)\n"
        "🌸 Adelfa (tóxica)"
    )

# 🖼️ EJEMPLOS
import random

@bot.command()
async def ejemplos(ctx):
    try:
        ejemplos = [
            {
                "nombre": "🍎 Manzano (comestible)",
                "ruta": "ejemplos/manzanas.jpg"
            },
            {
                "nombre": "🌸 Adelfa (tóxica)",
                "ruta": "ejemplos/adelfa.jpg"
            }
        ]

        elegido = random.choice(ejemplos)

        await ctx.send(
            content=elegido["nombre"],
            file=discord.File(elegido["ruta"])
        )

    except:
        await ctx.send("❌ No se encontraron imágenes")
# ================================
# RUN
# ================================
bot.run("")