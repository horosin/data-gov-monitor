# data-gov-monitor
Monitorowanie użycia witryny data.gov.pl

Projekt napisany jest w python3 oraz R.

W folderze data-analysis znajdują się skrypty odpowiedzialne za przetworzenie danych wejściowych - logów z serwera.
Jeśli nie posiadasz logów, możesz je zamockować. Wykorzystaj w tym celu skrypt mock-log-generator.py

Skrypt ip_reverse_scanner.py w oparciu o usługę ip-api.com uzyskuje informacje na temat adresu ip pobranego z logów serwerowych - jego lokalizacji i opisu ewentualnej usługi web.

Aby wygenerować raport zawieraący statystyki należy uruchomić skrypt render_report.R, który wygeneruje raport na podstawie danych z folderu /data-analysis/log-data/ oraz /data/ . Raport wygenerowany zostanie w formacie .html.
