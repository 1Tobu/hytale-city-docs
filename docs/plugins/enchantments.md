# EnchantmentsPlugin

Enchantments verwaltet zufällige Verzauberungen, Upgrade-Rolls, Konflikte und verhaltensabhängige Itemeffekte. Core stellt Definitionen und gemeinsame Item-/Upgrade-Daten bereit.

## Öffentliche Schnittstelle

`EnchantmentsApi.service()` liefert den Dienst; `serviceOrEmpty()` ermöglicht optionale Integration. `EnchantmentsService` bietet unter anderem `upgradeAndRoll`, `rollSingleEnchantment`, `applyRollResultToItem`, `setEnchantments`, `getEnchantments`, `getEnchantmentKeys`, `getUpgradeLevel` und `applyBehaviors`.

Rolls berücksichtigen Itemtyp, vorhandene Verzauberungen und Upgradelevel. Die Itemausprägung wird in Metadaten unter dem Namensraum `hytale_city_enchantments` abgelegt. Solche Metadaten müssen bei Kopien, Reservierungen und Rückerstattungen erhalten bleiben.

## Nutzung und Grenzen

Jobs kann das Plugin bei Item-Upgrades optional einbinden. Verhalten wird über die Trigger-/Regelimplementierung und `enchantment-behaviors.json` angewendet; eine Definition alleine beweist nicht, dass jeder gewünschte Spieleffekt implementiert ist.

`/enchant item [enchantment] [value]` ist ein administrativer bzw. Test-Einstieg und wird der Gruppe `hytale:WorldEditor` zugeordnet. Er ist kein frei verfügbarer Spieler-Shop.
