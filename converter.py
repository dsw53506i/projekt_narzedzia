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

def zapisz_dane(dane, sciezka):
    try:
        with open(sciezka, 'w', encoding='utf-8') as f:
            json.dump(dane, f, indent=4, ensure_ascii=False)
        print(f"Task3 sukces: Zapisano plik JSON do {sciezka}")
    except Exception as e:
        print(f"Blad zapisu pliku: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Blad: Niepoprawna liczba argumentow!")
        sys.exit(1)
        
    dane = wczytaj_dane(sys.argv[1])
    zapisz_dane(dane, sys.argv[2])

if __name__ == "__main__":
    main()