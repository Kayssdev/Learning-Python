from pathlib import Path

pasta = Path("/home/kay")
for arquivo in pasta.rglob("*.*"):
    if arquivo.is_file():
        print(arquivo)