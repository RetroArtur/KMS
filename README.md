Dies ist eine Komplettlösung zur Verarbeitung, Vektorisierung und Verwaltung von Dokumenten. Die Anwendung kombiniert eine Chat-Oberfläche, eine Vektordatenbank, einen automatisierten n8n Workflow sowie einen KMS-Dateimanager, der auf Flask basiert. Außerdem besteht die Möglichkeit, Zotero-Bibliotheken zu importieren und verlinkte Dokumente automatisch herunterzuladen und einzubinden.

---
## Überblick

Die Anwendung ermöglicht es, Dokumente (PDF, MD) zentral zu verwalten und in eine Vektordatenbank (Qdrant) einzubinden. Eine Chat-Oberfläche (OpenWebUI) erlaubt die Interaktion mit den eingebundenen Inhalten, während ein n8n Workflow den automatisierten Import und die Vektorisierung übernimmt. Über den KMS-Dateimanager können Benutzer Dateien hochladen, löschen und verwalten sowie Zotero-Bibliotheken importieren, um verlinkte Dokumente automatisch herunterzuladen.

---
## Installation

Nacherfolgreichem clonen des Repositories und ausführen der Dockerumgebung sind folgende Schritte erforderlich:

---
### 1. Umgebungsvariablen anpassen  
- Die Datei `.env.txt` in `.env` umbenennen.  
- Inhalte nach Bedarf anpassen.  

### 2. Workflow in n8n importieren  
- In n8n unter **"Create Workflow" → "Import from File"** den Workflow importieren.  
- Die Datei **`My_Workflow.json`** aus dem **Mount-Folder** auswählen.  

### 3. Workflow anpassen & Credentials setzen  
- Den importierten Workflow an den **Container** anpassen.  
- Die notwendigen **Credentials für externe Dienste** in n8n erstellen und ausfüllen.  

### 4. n8n in OpenWebUI als Funktion einbinden  
- In **OpenWebUI** unter **"Administration" → "Funktionen"** die Datei **`n8n_pipe.py`** hinzufügen.  
- In **`n8n_pipe.py`** die **Webhook-URL** mit der URL des n8n-Webhooks ersetzen.  

### Wichtiger Hinweis  
Da der Webhook häufig einen Timeout verursacht, sollte die Seite in OpenWebUI **während der Generierung der Antwort einmalig neu geladen werden**, damit die Antwort korrekt angezeigt wird.

---
## Architektur und Komponenten

Die Anwendung setzt sich aus folgenden Hauptkomponenten zusammen:

- **Chat-Oberfläche:** Bereitgestellt über OpenWebUI, dient als Frontend zur Interaktion mit den eingebundenen Dokumenten.
- **Vektordatenbank:** Dokumente werden in Qdrant gespeichert und vektorisiert. 
- **n8n Workflow:** Automatisiert den Import von Dateien aus dem Docker-Ordner `/data/shared/Exports`, die Vektorisierung dieser Dokumente in Qdrant und die Generierung der Antworten des phi4-KI-Modells.
- **KMS-Dateimanager:** Ein Flask-basiertes Python-Skript, das als Datei-Manager fungiert. Über diesen Manager können Dateien (PDF, MD) hochgeladen, eingesehen und gelöscht werden. Der Manager zeigt alle Dateien im Docker-Ordner `/data/shared/Exports` an.

---
## Einzelne Endpunkte & Zugriff

### Chat-Oberfläche (OpenWebUI)

- **URL:** [http://localhost:3000](http://localhost:3000)
- **Funktion:** Interaktion durch eine KI mit den im Vektor-Store eingebundenen Dokumenten über eine benutzerfreundliche Chat-Oberfläche.

### Vektordatenbank (Qdrant)

- **Dashboard URL:** [http://localhost:6333/dashboard](http://localhost:6333/dashboard) 
- **Funktion:** Speicherung und Verwaltung der Vektoren, die aus den Dokumenten generiert werden.

### n8n Workflow

- **URL:** [http://localhost:5678/workflow](http://localhost:5678/workflow) 
- **Name:** "My workflow"
- **Funktion:** Automatisierter Import von Dateien aus dem Ordner `/data/shared/Exports` und deren Vektorisierung in Qdrant, sowie Antwortengenerierung durch KI-Modelle.

### KMS-Dateimanager

- **URL:** [http://localhost:5000](http://localhost:5000)
- **Funktion:** 
	- Anzeige aller wichtigen Dateien im Ordner `/data/shared/Exports`.
	- Upload und Löschung von Dateien (PDF, MD).
	- Verwaltung der Dokumente, die später vom n8n Workflow eingelesen und in Qdrant eingebunden werden.

---
## Funktionen & Features

### Kommunikation mit der KI

- **Funktion:**  
    Über die Chat-Oberfläche (OpenWebUI) können Benutzer Fragen zu den hochgeladenen und vektorisierten Dokumenten stellen. Die KI nutzt die in Qdrant gespeicherten Vektoren, um relevante Informationen bereitzustellen.

### Dateiupload und -löschung

- **Dateiformate:** MD und PDF. 
- **Funktion:** Über den KMS-Dateimanager können Benutzer Dateien hochladen und löschen. Alle hochgeladenen Dateien werden automatisch in den Docker-Ordner `/data/shared/Exports` geschrieben und anschließend vom n8n Workflow verarbeitet.

### Zotero Pull

- **Funktion:** Wenn ein Benutzer zuvor seine Zotero-Bibliothek als JSON heruntergeladen hat, kann diese JSON-Datei über den KMS-Dateimanager hochgeladen werden.
- **Prozess:** Nach dem Upload kann ein Zotero Pull durchgeführt werden, der alle in der JSON verlinkten Dokumente herunterlädt und in das KMS integriert.

---
## Fehler und Lösungsansätze

Gängige Fehler und deren Lösungen werden in der Datei [Fehler und deren Lösungsansätze.md](Fehler%20und%20deren%20Lösungsans%C3%A4tze.md) dokumentiert. Bitte schaue dort nach, falls Probleme beim Upload, der Vektorisierung oder der Integration auftreten.

---
`Hinweis: Alle lokalen URLs (localhost) beziehen sich auf den Docker-Setup, der in ihrer Umgebung konfiguriert wurde.*`
