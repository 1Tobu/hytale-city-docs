# EnchantmentsPlugin

Enchantments manages random enchantments, upgrade rolls, conflicts, and behavior-driven item effects. Core provides definitions and shared item and upgrade data.

## Public interface

`EnchantmentsApi.service()` returns the service. Use `serviceOrEmpty()` for an optional integration. `EnchantmentsService` includes `upgradeAndRoll`, `rollSingleEnchantment`, `applyRollResultToItem`, `setEnchantments`, `getEnchantments`, `getEnchantmentKeys`, `getUpgradeLevel`, and `applyBehaviors`.

Rolls consider the item type, existing enchantments, and upgrade level. The resulting item state is stored under the metadata namespace `hytale_city_enchantments`. Preserve this metadata when copying, reserving, or refunding items.

## Usage and limitations

Jobs can integrate the plugin for upgrades. Effects run through the trigger and rule implementation and `enchantment-behaviors.json`. Check the behavior implementation for each effect you intend to use.

`/enchant item [enchantment] [value]` is an administrative or test command assigned to the `hytale:WorldEditor` group.
