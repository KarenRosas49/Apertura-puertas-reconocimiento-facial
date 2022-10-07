import argparse

parser = argparse.ArgumentParser()
parser.add_argument("img_src", help ="Imagen a buscar en la base de datos")
parser.add_argument("db_path", help = "Ruta de la base de datos")
args = parser.parse_args()

ruta = args.img_src + " " + args.db_path

print("Las rutas recibidas son: " + ruta)

#print(args.img_src)
#print(args.db_path)