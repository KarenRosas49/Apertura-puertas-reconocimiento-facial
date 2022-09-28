from deepface import DeepFace

print("Buscando rostro")

df = DeepFace.find(img_path = "/home/karen/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Imagen/timothee.jpeg", db_path = "/home/karen/Documents/GitHub/Apertura-puertas-reconocimiento-facial/my_db")

print("Resultado ")
print(df)