from deepface import DeepFace

obj = DeepFace.analyze(img_path = "//home/karen/Documents/GitHub/Apertura-puertas-reconocimiento-facial/Imagen/face.jpg", actions = ['age','gender','race','emotion'])
print("El resultado del analisis es: ")
print(obj)
