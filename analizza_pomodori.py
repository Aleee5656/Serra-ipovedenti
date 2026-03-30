import cv2
import numpy as np

def analizza_maturazione(image_path):
    # Carica l'immagine scattata dall'ESP32-CAM
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Definisci il range del colore ROSSO per i pomodori maturi
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    
    # Crea una maschera per isolare il rosso
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Calcola la percentuale di rosso nell'immagine
    red_pixel_count = np.sum(mask > 0)
    total_pixels = mask.size
    percentage = (red_pixel_count / total_pixels) * 100

    print(f"Percentuale maturazione: {percentage:.2f}%")

    # Logica di classificazione
    if percentage > 60:
        return "MATURI - Puoi raccogliere!"
    elif 30 <= percentage <= 60:
        return "IN MATURAZIONE - Aspetta ancora un po'."
    else:
        return "ACERBI - Ancora verdi."

# Esempio di utilizzo
# risultato = analizza_maturazione('foto_serra.jpg')
# print(risultato)
