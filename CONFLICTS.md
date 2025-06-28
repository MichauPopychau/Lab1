# Dokumentacja konfliktu między header-design-a oraz header-design-b

## Opis sytuacji

W projekcie powstały dwie gałęzie:
- `feature/header-design-a`
- `feature/header-design-b`

W obu zmodyfikowano ten sam fragment kodu w pliku `main.py` — linia nagłówka aplikacji.

## Szczegóły zmian

- W gałęzi `feature/header-design-a` nagłówek wyglądał tak:
print("=== Nagłówek A ===")
- W gałęzi `feature/header-design-b` nagłówek wyglądał tak:
print("=== Nagłówek B ===")

## Powstanie konfliktu

Podczas próby scalenia obu gałęzi z gałęzią `main` wystąpił konflikt, ponieważ Git nie był w stanie automatycznie stwierdzić, którą wersję nagłówka należy zachować.

## Rozwiązanie

Konflikt został rozwiązany ręcznie. Obie wersje zostały zamienione w jeden komunikat:
print("=== Nagłówek C ===")

Następnie plik został zapisany, a konflikt oznaczony jako rozwiązany przy pomocy komend:
git add main.py
git commit -m "Rozwiązano konflikt między header-design-a i header-design-b"
