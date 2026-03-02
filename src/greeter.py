def greet(name: str) -> str:
    return f"Hola, {name}!"

if __name__ == "__main__":
    nom = input("Como te llamas? ")
    print(greet(nom))
