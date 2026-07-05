import sys

def main():
    if len(sys.argv) != 3:
        print("Blad: Niepoprawna liczba argumentow!")
        print("Uzycie: program.exe plik1.ext plik2.ext")
        sys.exit(1)
    
    print(f"Parsowanie zakonczone sukcesem. Plik wejsciowy: {sys.argv[1]}, Wyjsciowy: {sys.argv[2]}")

if __name__ == "__main__":
    main()