from stegano import lsb

def nascondi_messaggio(percorso_immagine_input, percorso_immagine_output, messaggio_segreto):
    
    immagine_segreta = lsb.hide(percorso_immagine_input, messaggio_segreto) #Nasconde il messaggio nell'immagine
    immagine_segreta.save(percorso_immagine_output) #Salva l'immagine con il messaggio nascosto nella directory specificata
    print(f"Messaggio nascosto in {percorso_immagine_output}")

if __name__ == "__main__":
   
    percorso_immagine_input = '/home/kali/progetto_steganografia/immagine_copertura.png' #Directory immagine di copertura
    percorso_immagine_output = '/home/kali/progetto_steganografia/immagine_con_messaggio.png' #Directory immagine modificata
    messaggio_segreto = (
                        "Nascosto in piena vista: Steganografia è l'arte di mascherare i segreti dove tutti possono vedere ma nessuno sospetta."
                        "L'arte di vedere l'invisibile, sfidando l'occhio e la mente umana" #Creazione messaggio segreto
                        )
    nascondi_messaggio(percorso_immagine_input, percorso_immagine_output, messaggio_segreto)