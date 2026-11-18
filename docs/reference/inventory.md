# Plugin-Inventar und Quellstände

Inventar erzeugt am **2026-11-18**. Die Tabelle nennt den lokalen Commit, nicht einen behaupteten produktiven Deploymentstand.

Der Bericht exportiert ausschließlich ausgewählte Metadaten. Er liest keine produktiven Konfigurationsdateien oder Logs. Private Quellrepositories erfordern weiterhin eigene Zugriffsrechte.

[Inventar als JSON herunterladen](inventory.json).

| Plugin | Repository | Commit | Serverbereich |
| --- | --- | --- | --- |
| CorePlugin | `hytale-city-core-plugin` | [`c375b28`](https://github.com/1Tobu/hytale-city-core-plugin/commit/c375b2813ea3212154680427a5e838237220be54) | `^0.7.7` |
| CityBuildPlugin | `hytale-city-build-plugin` | [`38c0e94`](https://github.com/1Tobu/hytale-city-build-plugin/commit/38c0e9497fa64d49bc189f991c385e6a0653c45e) | `^0.7.7` |
| HomePlugin | `hytale-home-plugin` | [`ac917ae`](https://github.com/1Tobu/hytale-home-plugin/commit/ac917aee14dc540ab598278f04b447487eda6a24) | `^0.7.7` |
| EconomyPlugin | `hytale-money-system-plugin` | [`2390970`](https://github.com/1Tobu/hytale-money-system-plugin/commit/2390970146c959861369e8da4ba8f806fb3765d3) | `^0.7.7` |
| JobsPlugin | `hytale-jobs-plugin` | [`a78dd89`](https://github.com/nebbsen/hytale-jobs-plugin/commit/a78dd8988d22f5124b257a56d404132fb1cf6f86) | `^0.7.7` |
| LevelPlugin | `hytale-level-plugin` | [`54f7097`](https://github.com/1Tobu/hytale-level-plugin/commit/54f7097607d38494f41a2957299d412f11ea2a8d) | `^0.7.7` |
| HcNpcs | `HcNpcs` | [`77a509c`](https://github.com/nebbsen/HcNpcs/commit/77a509c7cd8bdee19580d7c5ec03c23d3b59fbfd) | `^0.7.7` |
| EnchantmentsPlugin | `hytale-city-enchantments` | [`6d78e4a`](https://github.com/nebbsen/hytale-city-enchantments/commit/6d78e4ac514b0cc13c8edcf49150de3231074d4b) | `^0.7.7` |
| PlayerStatsPlugin | `hytale-player-stats-plugin` | [`74b23c1`](https://github.com/1Tobu/PlayerStatsPlugin/commit/74b23c1436152b0264658c282f33afa6c9ad1a3c) | `^0.7.7` |
| PlayerHudPlugin | `hytale-playerhud-plugin` | [`d94de79`](https://github.com/nebbsen/hytale-playerhud-plugin/commit/d94de792f66baa6065d1051f1dc605cb636bdcc2) | `^0.7.7` |
| AfkPlugin | `hytale-afk-plugin` | [`183be31`](https://github.com/1Tobu/hytale-afk-plugin/commit/183be31bd4b2011257110de05ab57f0eb30d1a1f) | `^0.7.7` |
| TeleportPlugin | `hytale-teleport-plugin` | [`45bd8fd`](https://github.com/1Tobu/hytale-teleport-plugin/commit/45bd8fd233c6dc92eb05e166602a3811e119486d) | `^0.7.7` |
| WarpPlugin | `hytale-warp-plugin` | [`882fd9d`](https://github.com/1Tobu/hytale-warp-plugin/commit/882fd9df67b3b2759eecf5ed7eab0d642938b2de) | `^0.7.7` |
| FarmWorldPlugin | `hytale-farmworld-plugin` | [`f878a0a`](https://github.com/1Tobu/hytale-farmworld-plugin/commit/f878a0a50472792aeaf97f33eb7dc38eb195635a) | `^0.7.7` |
| ProtectionPlugin | `hytale-protection-plugin` | [`a0242ca`](https://github.com/1Tobu/hytale-protection-plugin/commit/a0242ca2740929459d09bdee493a3037ef43a831) | `^0.7.7` |
| DocumentationPlugin | `hytale-city-documentation-plugin` | [`fc90cb1`](https://github.com/1Tobu/hytale-city-documentation-plugin/commit/fc90cb16a9a540f8fac1268f6faa293865167b64) | `^0.7.7` |

## CorePlugin

Maven: `com.hytalecity:CorePlugin:1.0.0`.

Pflichtabhängigkeiten: keine deklariert.

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** keine im erfassten Bereich.

**API-Klassen:** keine im erfassten Bereich.

**Services:** `AsyncLevelService`, `HomeService`, `ItemEnchantmentService`, `ItemService`, `JobItemTotalService`, `JobItemUnlockService`, `JobMerchantQueryService`, `JobMilestoneClaimService`, `JobMilestoneDefinitionService`, `JobSaleService`, `JobService`, `JobXpProgressService`, `LevelProgressionService`, `LevelRewardService`, `NpcDefinitionService`, `PlayerLevelService`, `PlayerService`, `PlayerStatsBatchService`, `PlayerStatsService`, `PlotCoOwnerService`, `PlotInviteService`, `PlotMenuService`, `PlotOfferService`, `PlotService`, `ProtectionService`, `RankService`.

**UI-Dokumente:** keine im erfassten Bereich.

## CityBuildPlugin

Maven: `com.hytalecity:CityBuildPlugin:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`).

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** `PlotCommand`, `PlotsCommand`, `BuySubCommand`, `InfoSubCommand`, `InviteAcceptSubCommand`, `InviteCancelSubCommand`, `InviteDenySubCommand`, `InvitesSubCommand`, `InviteSubCommand`, `LimitGetSubCommand`, `LimitIncreaseSubCommand`, `LimitResetSubCommand`, `LimitSetSubCommand`, `LimitSubCommand`, `ListSubCommand`, `OfferAcceptSubCommand`, `OfferCancelSubCommand`, `OfferDenySubCommand`, `OffersSubCommand`, `OfferSubCommand`, `RenameSubCommand`, `SellToCitySubCommand`.

**API-Klassen:** keine im erfassten Bereich.

**Services:** keine im erfassten Bereich.

**UI-Dokumente:** `Common/UI/Custom/Plots/Plots.ui`.

## HomePlugin

Maven: `com.hytalecity:HomePlugin:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`).

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** `HomeCommand`, `HomesCommand`, `SetHomeCommand`, `HomeRemoveSubCommand`.

**API-Klassen:** keine im erfassten Bereich.

**Services:** keine im erfassten Bereich.

**UI-Dokumente:** `Common/UI/Custom/Homes/Homes.ui`.

## EconomyPlugin

Maven: `com.hytalecity:EconomyPlugin:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`).

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** `MoneyCommand`, `MoneyAddSubCommand`, `MoneyRemoveSubCommand`, `MoneySendSubCommand`, `MoneySetSubCommand`.

**API-Klassen:** keine im erfassten Bereich.

**Services:** keine im erfassten Bereich.

**UI-Dokumente:** keine im erfassten Bereich.

## JobsPlugin

Maven: `com.hytalecity:JobsPlugin:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`), `HytaleCity:HcNpcs` (`*`).

Optionale Abhängigkeiten: `HytaleCity:EnchantmentsPlugin` (`*`).

**Command-Klassen:** `JobCommand`, `JobAdminItemAddSubCommand`, `JobAdminMilestonesUiSubCommand`, `JobAdminNpcSetSubCommand`, `JobAdminShopUiSubCommand`, `JobAdminSubCommand`, `JobAdminUpgradeUiSubCommand`, `JobEnterSubCommand`, `JobInfoSubCommand`, `JobSellSubCommand`.

**API-Klassen:** `JobsAPI`, `JobUpdateListener`.

**Services:** `EnchantmentsBridgeService`, `JobMilestoneRuntimeService`, `JobShopOfferService`, `JobUpgradeRecipeService`, `NpcJobKeyService`.

**UI-Dokumente:** `Common/UI/Custom/Jobs/JobNpc.ui`, `Common/UI/Custom/Jobs/JobShopAdmin.ui`, `Common/UI/Custom/Jobs/JobUpgradeAdmin.ui`, `Common/UI/Custom/Jobs/JobUpgradeSelect.ui`, `Common/UI/Custom/Jobs/Jobs.ui`, `Common/UI/Custom/Jobs/MilestoneAdmin.ui`, `Common/UI/Custom/Jobs/MilestoneRow.ui`.

## LevelPlugin

Maven: `com.hytalecity:LevelPlugin:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`).

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** keine im erfassten Bereich.

**API-Klassen:** keine im erfassten Bereich.

**Services:** `LevelService`.

**UI-Dokumente:** keine im erfassten Bereich.

## HcNpcs

Maven: `com.hytalecity:HcNpcs:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`).

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** `NpcCommand`.

**API-Klassen:** `HcNpcsAPI`, `HcNpcsService`, `NpcActionHandler`, `Registration`.

**Services:** `HcNpcsService`.

**UI-Dokumente:** `Common/UI/Custom/HcNpcs/ActionRow.ui`, `Common/UI/Custom/HcNpcs/Actions.ui`.

## EnchantmentsPlugin

Maven: `com.hytalecity:EnchantmentsPlugin:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`).

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** `EnchantItemCommand`.

**API-Klassen:** `EnchantmentsApi`.

**Services:** `EnchantmentBehaviorService`, `EnchantmentsService`, `EnchantmentValueService`, `ItemUpgradeRollService`, `MoneyFindRewardService`.

**UI-Dokumente:** keine im erfassten Bereich.

## PlayerStatsPlugin

Maven: `com.hytalecity:PlayerStatsPlugin:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`).

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** keine im erfassten Bereich.

**API-Klassen:** keine im erfassten Bereich.

**Services:** keine im erfassten Bereich.

**UI-Dokumente:** keine im erfassten Bereich.

## PlayerHudPlugin

Maven: `com.hytalecity:PlayerHudPlugin:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`).

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** `HudCommand`.

**API-Klassen:** keine im erfassten Bereich.

**Services:** `HudService`.

**UI-Dokumente:** `Common/UI/Custom/Hud/PlayerHud.ui`.

## AfkPlugin

Maven: `com.hytalecity:AfkPlugin:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`).

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** keine im erfassten Bereich.

**API-Klassen:** keine im erfassten Bereich.

**Services:** `AfkDisconnectService`, `AfkService`.

**UI-Dokumente:** keine im erfassten Bereich.

## TeleportPlugin

Maven: `com.hytalecity:TeleportPlugin:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`).

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** `TpAcceptCommand`, `TpaCommand`, `TpDenyCommand`.

**API-Klassen:** keine im erfassten Bereich.

**Services:** `TpaService`.

**UI-Dokumente:** keine im erfassten Bereich.

## WarpPlugin

Maven: `com.hytalecity:WarpPlugin:1.0.0`.

Pflichtabhängigkeiten: keine deklariert.

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** `CitySubCommand`, `FarmWorldSubCommand`, `SpawnSubCommand`, `WarpCommand`.

**API-Klassen:** keine im erfassten Bereich.

**Services:** keine im erfassten Bereich.

**UI-Dokumente:** keine im erfassten Bereich.

## FarmWorldPlugin

Maven: `com.hytalecity:FarmWorldPlugin:1.0.0`.

Pflichtabhängigkeiten: keine deklariert.

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** keine im erfassten Bereich.

**API-Klassen:** keine im erfassten Bereich.

**Services:** `FarmWorldService`.

**UI-Dokumente:** keine im erfassten Bereich.

## ProtectionPlugin

Maven: `com.hytalecity:ProtectionPlugin:1.0.0`.

Pflichtabhängigkeiten: `HytaleCity:CorePlugin` (`*`).

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** `ProtectionCommand`, `ListSubCommand`, `RegisterSubCommand`, `RemoveSubCommand`.

**API-Klassen:** keine im erfassten Bereich.

**Services:** keine im erfassten Bereich.

**UI-Dokumente:** keine im erfassten Bereich.

## DocumentationPlugin

Maven: `com.hytalecity:DocumentationPlugin:1.0.0`.

Pflichtabhängigkeiten: keine deklariert.

Optionale Abhängigkeiten: keine deklariert.

**Command-Klassen:** `RulesCommand`, `TutorialCommand`.

**API-Klassen:** keine im erfassten Bereich.

**Services:** `DocumentationService`.

**UI-Dokumente:** `Common/UI/Custom/Rules/Rules.ui`, `Common/UI/Custom/Tutorial/Tutorial.ui`.
