from stegano import lsb

def rivela_messaggio(percorso_immagine):
    
    messaggio_rivelato = lsb.reveal(percorso_immagine) #Rivela messaggio nascosto nell'immagine
    return messaggio_rivelato

if __name__ == "__main__":
    percorso_immagine = '/home/kali/progetto_steganografia/immagine_con_messaggio.png' #Directory in cui l'immagine si trova
    messaggio_rivelato = rivela_messaggio(percorso_immagine)
    print(f"Il messaggio nascosto è: '{messaggio_rivelato}'")