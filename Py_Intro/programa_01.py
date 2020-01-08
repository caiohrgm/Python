import sys

sys.stdout.write("Digite uma frase:")
frase = sys.stdin.readline()
sys.stdout.write("Digite um numero:")
num_string = sys.stdin.readline()

num = int(num_string)
palavras = frase.split()
palavra = palavras[num - 1].upper()
msg = "A %da palavra da frase e: %s\n" % (num, palavra)

sys.stdout.write(msg)