import sys

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Error: Archivo '{filename}' no encontrado.")
        return []

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Se necesita un archivo que leer")
        exit(1)
    if len(sys.argv) > 2:
        print("Es necesario un unico archivo")
        exit(1)
    filename = sys.argv[1]
    lines = read_file(filename)
    contador = 0
    if lines:
        for line in lines:
            if line.startswith('#') or len(line.strip()) == 0:
                contador = contador + 1
        lineas_contadas = len(lines) - contador
        print (lineas_contadas)


