from stegano import lsb 

secret= lsb.hide("./immagine_copertura.png", "Nascosto in piena vista: Steganografia è l'arte di mascherare i segreti dove tutti possono vedere ma nessuno sospetta."
                                            "L'arte di vedere l'invisibile, sfidando l'occhio e la mente umana") 
secret.save("./immagine_con_messaggio.png")