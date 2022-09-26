from deepface import DeepFace

result = DeepFace.verify(img1_path = "/home/karen/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Imagen/timothee1.jpeg", img2_path = "/home/karen/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Imagen/timothee2.jpeg")

print("Resultados")
print(result)