# Updates und Wiederherstellung

## Vor dem Austausch

Versionen und Manifest-Abhängigkeiten prüfen. Core/HcNpcs/Jobs als kompatiblen Verbund behandeln. DB und betroffene Welten/Konfigurationen sichern. Eine bloß existierende Sicherungsdatei ist noch kein Nachweis einer erfolgreichen Wiederherstellung.

Auf dem Testserver Start, Schemaänderungen, Migration, NPCs, Verkäufe und UIs kontrollieren. Erst danach dieselben gebauten JARs verwenden. Eine Prüfsumme kann bestätigen, dass lokale und kopierte JAR übereinstimmen.

## Migrationen

- Allgemeine Spielerlevel: Legacy-JSON wird über Core importiert, danach ist die DB führend. Alte Dateien als Sicherung behalten.
- Job-NPCs: `jobs_npc_job_keys` wird idempotent in Core-Definitionen/-Aktionen importiert. Vorhandene Definitionen haben Vorrang, auch wenn eine Aktion absichtlich entfernt wurde.
- Job-Versionsprüfung: Schema-Update ergänzt `player_jobs.version` mit Default nullfreien Werten für vorhandene Daten; die Implementierung verwendet den SQL-Default `0`.

Legacy-NPC-Definitionen nicht einfach löschen, um einen NPC abzuschalten: Sonst kann eine alte Zuordnung bei einem erneuten Import wieder auftauchen. Die Definition deaktivieren bzw. die Aktion gezielt entfernen.

## Offene Verkäufe

| Zustand | Bedeutung / Maßnahme |
| --- | --- |
| `PREPARED` | Entnahme möglicherweise erfolgt; Inventarplan und echten Bestand prüfen |
| `COMMITTED` | DB-Belohnungen verbucht; nicht blind Items zurückgeben |
| `REFUND_DUE` | Rückerstattung offen oder teilweise erfolgt; tatsächliche Erstattung abgleichen |
| `ABORTED` | Kein Auszahlungsvorgang mehr offen und Rückgabe/ausgebliebene Entnahme bestätigt |

`JobSaleService.pending`, `diagnostic`, `commit`, `abort` und `confirmRefund` unterstützen eine ausdrückliche Prüfung. Die Bestätigung einer Rückgabe darf erst nach tatsächlicher Rückgabe oder nachgewiesener Nichtentnahme erfolgen. Ein wiederholter `abort` autorisiert keine zweite physische Rückgabe.

Inventar- und Weltdateien lassen sich nicht zusammen mit MariaDB atomar committen. Bei unklarem Prozessabbruch deshalb anhand der Vorgangs-ID prüfen, statt automatisch den ganzen Plan zu erstatten. [Vollständiger Vertrag](../reference/npc-contracts.md).
