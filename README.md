# VORTRAEGS-SPICKZETTEL:

LLM LOKAL HOSTEN (VERSION 2026)

I.  WARUM EINE KI LOKAL BETREIBEN?

- Datenschutz: Deine Daten verlassen dein Zuhause oder dein Netzwerk nicht. Keine Analyse durch Cloud-Anbieter.
- Volle Kontrolle: Du entscheidest, welches Modell laeuft, wie lange die Daten gespeichert werden und wer Zugriff hat.
- Unabhaengigkeit: Keine monatlichen Abos, keine Internetabhaengigkeit fuer die Kernfunktion und keine Zensur durch Drittanbieter.

II.  WAS IST EIN LLM-HOST? (ANALOGIE)

- Die Wohnung: Ein KI-Modell (das LLM) ist wie ein Bewohner, der einen Ort zum Leben und Arbeiten braucht.
- Ollama: Das ist die Infrastruktur (der Host), die das Modell verwaltet und die Kommunikation ermoeglicht.
- Open Source: Ollama wird unter der freien MIT-Lizenz entwickelt. Quelle: [github.com/ollama/ollama](https://github.com/ollama/ollama)

III.  DIE WAHL DES BETRIEBSSYSTEMS: WARUM LINUX? Fuer einen stabilen 24/7-Betrieb bietet Linux (z. B. Ubuntu oder Debian) massive Vorteile:

- Headless-Betrieb (Ohne Grafikoberflaeche): In einem System ohne Fenster und Maus wird kein RAM fuer die Anzeige verschwendet.
- Ressourcen-Maximierung: Fast der gesamte Arbeitsspeicher steht der KI zur Verfuegung.
- Effizienz: Der Prozessor muss keine Pixel berechnen, sondern konzentriert sich rein auf die Textgenerierung.
- Fernsteuerung: Das System steht kompakt in einer Ecke und wird bequem per Netzwerk (SSH) bedient.

IV.  HARDWARE-ANFORDERUNGEN Beim Thema KI ist RAM (Arbeitsspeicher) die wichtigste Kennzahl.

- Erste Schritte: Ein Einplatinencomputer (z.B. Raspberry Pi 5 mit 8 GB) reicht fuer Experimente aus (ca. 3-5 Woerter/Sek).
- Effizienz-Tipp: Mac Mini M4 (ab 16 GB RAM). Extrem stromsparend, nutzt "Unified Memory" ideal fuer KI aus. Oft guenstiger im Betrieb als alte Grafikkarten.
- Performance-Tipp: NVIDIA RTX 5060 Ti (16 GB VRAM). Die moderne Wahl fuer 2026. Sehr schnell und zukunftssicher durch Blackwell-Architektur.
- Faustregel: Je groesser das Modell, desto mehr RAM/VRAM wird benoetigt (ca. 1 GB pro 1 Mrd. Parameter).

V.  INSTALLATION & ERSTER START Die Installation unter Linux ist dank eines offiziellen Skripts einfach:

- Der Installations-Einzeiler ueber das Terminal:
- 
- curl -fsSL https://ollama.com/install.sh | sh
- 
- Das Skript erkennt automatisch die Hardware und richtet Ollama als Hintergrunddienst ein.
- Das erste Modell laden: ollama run llama3.2:1b (Das Modell "1b" ist klein, schnell und ideal fuer kompakte Hardware.)

VI.  SCHNITTSTELLEN ZUR KI

- CLI (Command Line Interface): Direktes Chatten im Text-Terminal.
- API-Server: Eingebauter Server (Port 11434), um Weboberflaechen oder Handy-Apps anzubinden.

VII.  KLEINES KI-GLOSSAR (FUER RUECKFRAGEN)

- LLM (Large Language Model): Das "Gehirn" der KI, das mit Textmengen trainiert wurde.
- Token: Ein "Wortstueck". Geschwindigkeit wird in Tokens pro Sekunde (tk/s) gemessen.
- Parameter: Die Anzahl der Verbindungen im Modell (z.B. 1b, 8b). Mehr = klueger, aber hardwarehungriger.
- VRAM (Video RAM): Der Speicher auf der Grafikkarte. Entscheidend fuer die KI-Geschwindigkeit.
- Unified Memory: Gemeinsamer Speicher von CPU und Grafik (Apple M-Chips), sehr effizient fuer KI.
- SSH (Secure Shell): Die Fernsteuerung fuer Rechner ohne Monitor ueber das Netzwerk.

MERKBLATT FUER DIE DEMO (KURZBEFEHLE):

- ollama list -> Zeigt alle heruntergeladenen Modelle an.
- ollama ps -> Zeigt an, welches Modell gerade im Speicher aktiv ist.
- top oder htop -> Um die Auslastung von CPU und RAM live zu sehen.

- - 
-
