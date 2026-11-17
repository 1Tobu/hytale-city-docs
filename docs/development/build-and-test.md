# Bauen und prüfen

## Plugin-JARs

Die aktuellen Repositories verwenden Maven-Wrapper und Java 25, nicht das alte Gradle-Template aus früheren READMEs.

```powershell
$env:JAVA_HOME = 'C:/PFAD/ZUM/JDK-25'
.\mvnw.cmd clean install
```

Core zuerst lokal installieren, damit abhängige Plugins seine aktuellen Klassen erhalten. Für den NPC-Verbund danach HcNpcs installieren und Jobs paketieren:

```text
Core:   mvnw.cmd clean install
HcNpcs: mvnw.cmd clean install
Jobs:   mvnw.cmd clean package
```

Die auszuliefernden Artefakte liegen unter `target/`, beispielsweise `CorePlugin-1.0.0.jar`, `HcNpcs-1.0.0.jar` und `JobsPlugin-1.0.0.jar`. Beim Core die fertige gebündelte JAR verwenden, nicht `original-CorePlugin-1.0.0.jar`.

`clean` ist bei entfernten oder umbenannten Klassen wichtig, damit keine alten Listener-/Debug-Klassen in der JAR verbleiben. Maven-Abhängigkeit `0.7.7` und Manifest-Bereich `^0.7.7` erfüllen unterschiedliche Syntaxverträge.

## Aussagekraft der Prüfungen

Die zuletzt geprüfte NPC-Änderung hatte 54 Core-, drei HcNpcs- und sechs Jobs-Tests ohne Fehler. Das ist ein dokumentierter Prüfstand, kein automatisch fortgeschriebener Zähler. Die Tests umfassen unter anderem Transaktionsrollback, Wiederholungen, parallele Geld-/XP-Änderungen und exakte Inventarpläne.

H2-Tests ersetzen keine MariaDB-Abnahme. Die vorhandenen Java-/Maven-Tests prüfen ebenfalls keine echte Hytale-UI-Darstellung und keine vollständige Weltinstanziierung. Diese Pfade auf einem Testserver prüfen und den konkreten Serverbuild zum Ergebnis festhalten.

## Dokumentation

```text
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
python -m mkdocs serve
```

Der Dokumentationsworkflow verändert oder baut keine privaten Gameplay-Repositories. Er veröffentlicht nur den öffentlichen Dokumentationsinhalt.
