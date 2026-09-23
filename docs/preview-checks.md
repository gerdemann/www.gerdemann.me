# Lokale Abnahme – 14. September 2026

- Hugo 0.166.0 extended: lokaler Build ohne Fehler oder Warnungen.
- 196 bestehende Inhalts-/Bild-/Feed-URLs geprüft; 45 alte Paginierungsadressen liefern HTTP 301 zum vollständigen Archiv.
- 62 HTML-Seiten, 263 interne Links/Assets und 22 RSS-Einträge geprüft.
- Bestehende Überschriftenanker erhalten; genau eine H1 je Seite, lokale Canonicals und Beschreibungen vorhanden.
- Nicht existierende URL liefert HTTP 404. Vorschau ist mit noindex und robots.txt ausgeschlossen.
- Keine extern geladenen Skripte, Stylesheets oder Frames in den geprüften Seiten; Tracking und Giscus sind lokal deaktiviert.
- Startseite, Profil, Blogarchiv sowie Artikel mit Bildern und Code bei 375, 768 und 1440 Pixeln geprüft: keine horizontale Seitenausdehnung.
- Heller und dunkler Modus visuell geprüft; Auswahl bleibt bei Seitennavigation erhalten.
- Mobiles Menü öffnet und schließt; Escape setzt den Fokus zurück auf den Menüknopf. Tastaturnavigation erreicht die Inhaltslinks. Codeblöcke sind fokussierbar.
- Projektsprung per Link geprüft. Artikel zeigen Datum, Lesedauer, Inhaltssprache, Tags und den lokalen Kommentarhinweis.
- Start-/Stoppskript erprobt. Laufender Server ausschließlich an 127.0.0.1:1313 gebunden.
- git diff --check erfolgreich. Deployment-Workflow, Dockerfile und produktive Serverkonfiguration unverändert.

## Grenzen dieser Vorschau

Kein produktives Deployment, kein Push, kein Test mit realen externen Kommentaren.
Externe Projektlinks wurden aus dem vorhandenen Profil übernommen; deren aktueller
Betriebsstatus ist nicht Teil der lokalen Abnahme. Kein vollständiges WCAG-Audit und
keine Lighthouse-Messung. Der URL-Bestand stammt aus dem unveränderten Repository,
nicht aus historischen Webserver-Zugriffsprotokollen.
