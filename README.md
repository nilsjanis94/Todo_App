# Todo App

Eine moderne Todo-Anwendung zum Verwalten und Organisieren deiner täglichen Aufgaben, entwickelt mit Django.

## Funktionen

- Erstellen, Bearbeiten und Löschen von Aufgaben
- Übersichtliche Anzeige aller Aufgaben
- Markieren von Aufgaben als erledigt
- Aufgaben mit Titel, Beschreibung und Erstellungsdatum

## Technologien

- Backend: Django 5.2
- Datenbank: SQLite
- Frontend: HTML, CSS, Django Templates

## Installation

1. Repository klonen:
```bash
git clone https://github.com/dein-username/todo-app.git
cd todo-app
```

2. Virtuelle Umgebung erstellen und aktivieren:
```bash
# Erstellen
python -m venv venv

# Aktivieren (Windows)
venv\Scripts\activate

# Aktivieren (macOS/Linux)
source venv/bin/activate
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

4. Datenbank migrieren:
```bash
python manage.py migrate
```

5. Entwicklungsserver starten:
```bash
python manage.py runserver
```

Die Anwendung ist nun unter [http://localhost:8000](http://localhost:8000) verfügbar.

## Projektstruktur

```
├── meinprojekt/       # Django Projekteinstellungen
├── meineapp/          # Todo-App Anwendung
│   ├── migrations/    # Datenbankmigrationen
│   ├── static/        # CSS, JavaScript, Bilder
│   ├── templates/     # HTML-Templates
│   ├── admin.py       # Admin-Konfiguration
│   ├── forms.py       # Formular-Definitionen
│   ├── models.py      # Datenmodelle
│   ├── tests.py       # Tests
│   ├── urls.py        # URL-Routing
│   └── views.py       # View-Funktionen
├── venv/              # Virtuelle Python-Umgebung
├── manage.py          # Django-Verwaltungsskript
├── db.sqlite3         # SQLite-Datenbank
└── requirements.txt   # Projektabhängigkeiten
```

## Nutzung

- Öffne die Anwendung im Browser unter [http://localhost:8000](http://localhost:8000)
- Neue Aufgabe erstellen: Klicke auf den "Aufgabe hinzufügen" Button
- Aufgabe als erledigt markieren: Klicke auf die Checkbox neben der Aufgabe
- Aufgabe bearbeiten: Klicke auf den "Bearbeiten" Link bei der entsprechenden Aufgabe
- Aufgabe löschen: Klicke auf den "Löschen" Link

## Administration

Ein Admin-Interface ist unter [http://localhost:8000/admin](http://localhost:8000/admin) verfügbar.

Um einen Admin-Benutzer zu erstellen:
```bash
python manage.py createsuperuser
```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe [LICENSE](LICENSE) für Details.
