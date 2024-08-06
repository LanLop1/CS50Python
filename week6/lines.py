import sys

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print("File does not exist.")
        return []

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        exit(1)
    filename = sys.argv[1]
    if not filename.endswith(".py"):
        print("Not a Python file")
        exit(1)
    lines = read_file(filename)
    contador = 0
    if lines:
        for line in lines:
            line.strip()
            if line.startswith('#') or len(line.strip()) == 0:
                contador = contador + 1
        lineas_contadas = len(lines) - contador
        print (lineas_contadas)


