## Chatbot-Fehler

- Antworten auf Englisch
	- **Grund**: Halluzination nach System-Prompt, Modell (phi4) noch nicht perfekt auf deutsch
	- **Lösung**: Prompt erneut eingaben, notfalls mit Aufforderung auf deutsch zu antworten
- Keine Antwort erscheint, Lange Ladezeit der Antwort
	- **Grund**: Pro Antwort werden ca. 30-40 sek. gebraucht, oft deshalb Timeout des Webhooks
	- **Lösung**: Seite neu laden, idealerweise während die Antwort noch lädt.
- Antwort nicht akkurat genug
	- **Grund**: Kann nur ein Themengebiet pro Prompt genau erläutern auf Grund des Query-Aufbaus
	- **Lösung**: Komplexere Themenbereiche in mehrere Fragen aufteilen
- Kein Zitat in der Antwort
	- **Grund**: Keine Quelle gefunden, Halluzination
	- **Lösung**: Frage erneut bzw. neu formulieren


## Datei/Workflow-Fehler

- Conflict bei Vektorisierung beim Upload
	- **Grund**: Zu große parallele Vektorisierung
	- **Lösung**: `time.sleep(x);` in der zotero_pull.py erhöhen oder Dateien einzeln und langsam nacheinander hochladen
- Uploadfehler wegen Dateigröße
	- **Grund**: Zu große Menge für Embedding-Modell
	- **Lösung**: Datei manuell in mehrere Teile aufteilen, Leistungstärkeres Modell und GPU verwenden, über n8n Execution neustarten
- 


