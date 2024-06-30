from stegano import lsb

message = lsb.reveal("./immagine_con_messaggio.png")
print(message)