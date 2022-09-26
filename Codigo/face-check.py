from deepface import DeepFace

result = DeepFace.verify(img1_path = "/home/karen/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Imagen/face.jpg", img2_path = "/home/karen/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Imagen/Foto2.jpg")

print("Resultados")
print(result)