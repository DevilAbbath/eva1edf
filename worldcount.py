import sys

if len(sys.argv) != 2:
    print("Uso: python word_count.py <ruta_del_archivo>")
    sys.exit(1)

pathfile = sys.argv[1]

with open(pathfile, "r") as file:
    text = file.read()

difcharacter = set(text)
numberdifcharacter = len(difcharacter)

words = text.split()
difword = set(words)
numberdifword = len(difword)

print(f"El número de caracteres distintos es: {numberdifcharacter}")
print(f"El número de palabras distintas es: {numberdifword}")
