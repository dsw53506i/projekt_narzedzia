import sys
import os
import json

def wczytaj_dane(sciezka):
    if not os.path.exists(sciezka):
        print(f"Blad: Plik '{sciezka}' nie istnieje!")
        sys.exit(1)
    try:
        with open(sciezka, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Blad skladni JSON: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        sys.exit(1)
    dane = wczytaj_dane(sys.argv[1])
    print("Task2: JSON wczytany i zweryfikowany.")

if __name__ == "__main__":
    main()