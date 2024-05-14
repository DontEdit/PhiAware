# PhiAware
Dies ist eine einfache Flask-Webanwendung, die die Anzahl der Klicks auf verschiedene Links basierend auf Benutzergruppen (Professoren, wissenschaftliche Mitarbeiter und Studierende) verfolgt. Sie zeigt Nutzern die auf entsprechende Links geklickt haben im Anschluss eine Phishing Awareness Seite. Verwendet wird SQLAlchemy zur Datenbankverwaltung und zum Verfolgen von Linkklicks.

## Voraussetzungen
- Python 3.x
- Flask
- Flask-SQLAlchemy

## Einrichtung
1. **Clone das Repository:**
   - Klonen Sie das Repository mit dem bereitgestellten Code auf Ihrem lokalen System:
     ```
     git clone https://github.com/DontEdit/PhiAware.git
     ```

2. **Navigieren Sie in das Projektverzeichnis:**
   - Wechseln Sie in das Verzeichnis des geklonten Repositorys.

3. **Installieren Sie die erforderlichen Bibliotheken:**
   - Verwenden Sie `pip` und die `requirements.txt`-Datei im Repository, um die erforderlichen Bibliotheken zu installieren:
     ```
     pip install -r requirements.txt
     ```

4. **Starten Sie die Anwendung:**
   - Führen Sie die Flask-Anwendung aus:
     ```
     flask --app PhiAware run
     ```

## Funktionsweise
1. **Datenbankkonfiguration:**
- Die Anwendung verwendet SQLite zur Datenbankverwaltung.
- Beim Start der Flask App wird ein `/instance` Verzeichnis mit der `link_clicks.db` Datenbankdatei erstellt.

2. **Datenbankmodell:**
- Die Klasse `Click` in der `PhiAware.py` definiert die Struktur der Datenbanktabelle.
- Sie enthält drei Felder: `id` (Primärschlüssel), `group` (Zeichenfolge, die die Benutzergruppe repräsentiert) und `count` (Integer, der die Anzahl der Klicks repräsentiert).

3. **Routen:**
- **`/` (Index):** Rendert die Vorlage `index.html`, diese beinhaltet die Awareness Seite.
- **`/<group>/<path:url>` (click):** Behandelt Linkklicks. Inkrementiert die Klickzahl für die angegebene Gruppe und leitet den Benutzer zur Awareness Seite weiter.
- **`/<path:path>` (other_page):** Leitet Anfragen für jede andere Seite auf die Indexseite weiter.

4. **Klickverfolgung:**
- Wenn ein Benutzer einen Link anklickt (`/<group>/<path:url>`), überprüft die Anwendung, ob der Link für die angegebene Gruppe in der aktuellen Sitzung bereits angeklickt wurde.
- Wenn nicht, inkrementiert sie die Klickzahl für diese Gruppe und setzt ein Cookie, um den Link als angeklickt zu markieren.
- Wenn der Link bereits in der aktuellen Sitzung angeklickt wurde, leitet sie den Benutzer zurück zur Indexseite.
- Die hierfür verwendeten Cookies werden Client-Side gespeichert

5. **Fehlerbehandlung:**
- Wenn eine ungültige Gruppe angegeben wird, gibt die Anwendung eine Fehlermeldung aus und leitet den Nutzer auf die Awareness Seite weiter.


## Datenschutz
Um zu verhindern, dass Personen mehrfach auf einen Link klicken. Erhält jeder Teilnehmer einen individuellen Link. Dieser wird zufällig generiert, sodass zu keiner Zeit eine Übersicht darüber besteht, welche Person welchen Link hat.

Lediglich in der gesendeten E-Mail sind der Link und die Teilnehmer gemeinsam zu sehen. Allerdings lässt sich alleine aus der E-Mail nicht ableiten, ob der Link angeklickt wurde oder nicht. Hierfür sind zusätzlich die Server-Logs erforderlich, die anzeigen, ob eine URL aufgerufen wurde. 

Eine Datenbank speichert stets die Gesamtzahl der geklickten Links pro Gruppe und erlaubt keine Identifizierung einzelner Personen, die diese Links angeklickt haben.

Eine datenschutzkonforme Nutzung der Phishing-Awareness-Seite erfordert, dass die Person, die E-Mails versendet, keinen Zugriff auf die Server-Logs hat. Stattdessen sollte eine separate Person die Datenbankinhalte auswerten können. So wird sichergestellt, dass persönliche Informationen der Benutzer geschützt sind und nur autorisierte Personen Zugriff auf sensible Daten haben.