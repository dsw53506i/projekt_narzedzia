import sys
import os
import json
import yaml

def wczytaj_dane(sciezka):
    if not os.path.exists(sciezka):
        print(f"Blad: Plik '{sciezka}' nie istnieje!")
        sys.exit(1)
        
    rozszerzenie = sciezka.split('.')[-1].lower()
    
    try:
        if rozszerzenie == 'json':
            with open(sciezka, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif rozszerzenie in ['yml', 'yaml']:
            with open(sciezka, 'r', encoding='utf-8') as f:
                dane = yaml.safe_load(f)
                if dane is None:
                    raise yaml.YAMLError("Plik YAML jest pusty.")
                return dane
        else:
            print(f"Blad: Nieobslugiwany format wejsciowy: .{rozszerzenie}")
            sys.exit(1)
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        print(f"Blad skladni w pliku {sciezka}: {e}")
        sys.exit(1)

def zapisz_dane(dane, sciezka):
    rozszerzenie = sciezka.split('.')[-1].lower()
    try:
        if rozszerzenie == 'json':
            with open(sciezka, 'w', encoding='utf-8') as f:
                json.dump(dane, f, indent=4, ensure_ascii=False)
            print(f"Task3 sukces: Zapisano plik JSON do {sciezka}")
        elif rozszerzenie in ['yml', 'yaml']:
            with open(sciezka, 'w', encoding='utf-8') as f:
                yaml.dump(dane, f, default_flow_style=False, allow_unicode=True)
            print(f"Task5 sukces: Zapisano plik YAML do {sciezka}")
        else:
            print(f"Blad: Nieobslugiwany format wyjsciowy: .{rozszerzenie}")
            sys.exit(1)
    except Exception as e:
        print(f"Blad zapisu pliku {sciezka}: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Blad: Niepoprawna liczba argumentow!")
        sys.exit(1)
        
    dane = wczytaj_dane(sys.argv[1])
    zapisz_dane(dane, sys.argv[2])

if __name__ == "__main__":
    main()