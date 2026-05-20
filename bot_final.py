from os import environ
import threading
from flask import Flask
import telebot
import time
import random

# --- SISTEMA PARA O RENDER NÃO DESLIGAR O BOT ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Online"

def run_web():
    port = int(environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
# ------------------------------------------------

TOKEN = "8696750780:AAE64tA05ekvFJKvr_zWB9qHXCSCJf0yw20"
CANAL_ID = -1003945865350

bot = telebot.TeleBot(TOKEN)

def gerar_grid():
    # Trocamos '⬜' por '🟦'
    # '🟦' para os vazios e '*' para as estrelas
    grid = ['🟦'] * 22 + ['⭐'] * 3
    random.shuffle(grid)
    linhas = [grid[i:i+5] for i in range(0, 25, 5)]
    return "\n".join(["".join(linha) for line in linhas])

def gerar_sinal():
    minas = random.randint(1, 3)
    tentativas = random.randint(2, 3)
    grid_visual = gerar_grid()
    
    return (
        f"💣 **MINES HACKOWANY** 💣\n\n"
        f"🎯 Miny: `{minas}`\n"
        f"⏳ Ważny do: `19:50`\n"
        f"📊 Liczba prób: `{tentativas}`\n\n"
        f"{grid_visual}\n\n"
        f"🔗 **PLATFORMA HACKOWANA:** [TUTAJ](https://leon-poland.casino/registration?qtag=a44724_t59815_c3035_s)"
    )

print("Robô iniciado. A enviar sinais em polaco...")

# Liga o servidor falso em segundo plano para o Render ficar feliz
threading.Thread(target=run_web, daemon=True).start()

try:
    while True:
        texto_sinal = gerar_sinal()
        bot.send_message(CANAL_ID, texto_sinal, parse_mode="Markdown")
        print("Sinal enviado com sucesso!")
        
        # Espera entre 300s (5min) e 420s (7min)
        tempo_espera = random.randint(300, 420)
        time.sleep(tempo_espera)
        
except KeyboardInterrupt:
    print("Robô parado.")