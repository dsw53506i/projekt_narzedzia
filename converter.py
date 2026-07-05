# ... (reszta kodu bez zmian) ...
def zapisz_json(dane, sciezka):
    try:
        with open(sciezka, 'w', encoding='utf-8') as f:
            json.dump(dane, f, indent=4, ensure_ascii=False)
        print(f"Task3: Zapisano do JSON: {sciezka}")
    except Exception as e:
        print(f"Blad zapisu JSON: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3: sys.exit(1)
    dane = wczytaj_dane(sys.argv[1])
    zapisz_json(dane, sys.argv[2])

if __name__ == "__main__":
    main()