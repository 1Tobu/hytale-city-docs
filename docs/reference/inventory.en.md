# Plugin inventory and source revisions

Inventory generated on **2026-11-20**. The table reports the local commit recorded for each checkout.

The report exports selected metadata only. Access to private source repositories requires permission.

[Download the inventory as JSON](inventory.json).

| Plugin | Repository | Commit | Server version range |
| --- | --- | --- | --- |
| CorePlugin | `hytale-city-core-plugin` | [`d292436`](https://github.com/1Tobu/hytale-city-core-plugin/commit/d2924360521012880616dfa77ceb98e7557a1d11) | `^0.7.7` |
| CityBuildPlugin | `hytale-city-build-plugin` | [`263080f`](https://github.com/1Tobu/hytale-city-build-plugin/commit/263080fa3f78926f0297fe6ae73d0290c1dc605d) | `^0.7.7` |
| HomePlugin | `hytale-home-plugin` | [`ac917ae`](https://github.com/1Tobu/hytale-home-plugin/commit/ac917aee14dc540ab598278f04b447487eda6a24) | `^0.7.7` |
| EconomyPlugin | `hytale-money-system-plugin` | [`2390970`](https://github.com/1Tobu/hytale-money-system-plugin/commit/2390970146c959861369e8da4ba8f806fb3765d3) | `^0.7.7` |
| JobsPlugin | `hytale-jobs-plugin` | [`70bc47f`](https://github.com/nebbsen/hytale-jobs-plugin/commit/70bc47f18e6c4453054185288f35f640d9bd1360) | `^0.7.7` |
| LevelPlugin | `hytale-level-plugin` | [`54f7097`](https://github.com/1Tobu/hytale-level-plugin/commit/54f7097607d38494f41a2957299d412f11ea2a8d) | `^0.7.7` |
| HcNpcs | `HcNpcs` | [`f8929fd`](https://github.com/nebbsen/HcNpcs/commit/f8929fdcb57c29ab0272ddae785b962a27069188) | `^0.7.7` |
| EnchantmentsPlugin | `hytale-city-enchantments` | [`6d78e4a`](https://github.com/nebbsen/hytale-city-enchantments/commit/6d78e4ac514b0cc13c8edcf49150de3231074d4b) | `^0.7.7` |
| PlayerStatsPlugin | `hytale-player-stats-plugin` | [`74b23c1`](https://github.com/1Tobu/PlayerStatsPlugin/commit/74b23c1436152b0264658c282f33afa6c9ad1a3c) | `^0.7.7` |
| PlayerHudPlugin | `hytale-playerhud-plugin` | [`750e5f4`](https://github.com/nebbsen/hytale-playerhud-plugin/commit/750e5f4d72ef8bcde59c4e57c78bf19936b1fe32) | `^0.7.7` |
| AfkPlugin | `hytale-afk-plugin` | [`c7e598a`](https://github.com/1Tobu/hytale-afk-plugin/commit/c7e598a743b8ca6f974fcd73df03e8f34192a44b) | `^0.7.7` |
| TeleportPlugin | `hytale-teleport-plugin` | [`45bd8fd`](https://github.com/1Tobu/hytale-teleport-plugin/commit/45bd8fd233c6dc92eb05e166602a3811e119486d) | `^0.7.7` |
| WarpPlugin | `hytale-warp-plugin` | [`882fd9d`](https://github.com/1Tobu/hytale-warp-plugin/commit/882fd9df67b3b2759eecf5ed7eab0d642938b2de) | `^0.7.7` |
| FarmWorldPlugin | `hytale-farmworld-plugin` | [`f878a0a`](https://github.com/1Tobu/hytale-farmworld-plugin/commit/f878a0a50472792aeaf97f33eb7dc38eb195635a) | `^0.7.7` |
| ProtectionPlugin | `hytale-protection-plugin` | [`a0242ca`](https://github.com/1Tobu/hytale-protection-plugin/commit/a0242ca2740929459d09bdee493a3037ef43a831) | `^0.7.7` |
| DocumentationPlugin | `hytale-city-documentation-plugin` | [`fc90cb1`](https://github.com/1Tobu/hytale-city-documentation-plugin/commit/fc90cb16a9a540f8fac1268f6faa293865167b64) | `^0.7.7` |

## CorePlugin

Maven: `com.hytalecity:CorePlugin:1.0.0`.

Required dependencies: none declared.

Optional dependencies: none declared.

**Command classes:** none found.

**API classes:** none found.

**Services:** `AsyncLevelService`, `HomeService`, `ItemEnchantmentService`, `ItemService`, `JobCatalogService`, `JobItemTotalService`, `JobItemUnlockService`, `JobMerchantQueryService`, `JobMilestoneClaimService`, `JobMilestoneDefinitionService`, `JobSaleService`, `JobService`, `JobXpProgressService`, `LevelProgressionService`, `LevelRewardService`, `NpcDefinitionService`, `PlayerLevelService`, `PlayerService`, `PlayerStatsBatchService`, `PlayerStatsService`, `PlotCoOwnerService`, `PlotInviteService`, `PlotMenuService`, `PlotOfferService`, `PlotService`, `ProfessionService`, `ProtectionService`, `RankService`.

**UI documents:** none found.

## CityBuildPlugin

Maven: `com.hytalecity:CityBuildPlugin:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`).

Optional dependencies: none declared.

**Command classes:** `PlotCommand`, `PlotsCommand`, `BuySubCommand`, `InfoSubCommand`, `InviteAcceptSubCommand`, `InviteCancelSubCommand`, `InviteDenySubCommand`, `InvitesSubCommand`, `InviteSubCommand`, `LimitGetSubCommand`, `LimitIncreaseSubCommand`, `LimitResetSubCommand`, `LimitSetSubCommand`, `LimitSubCommand`, `ListSubCommand`, `OfferAcceptSubCommand`, `OfferCancelSubCommand`, `OfferDenySubCommand`, `OffersSubCommand`, `OfferSubCommand`, `RenameSubCommand`, `SellToCitySubCommand`.

**API classes:** none found.

**Services:** none found.

**UI documents:** `Common/UI/Custom/Plots/Plots.ui`.

## HomePlugin

Maven: `com.hytalecity:HomePlugin:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`).

Optional dependencies: none declared.

**Command classes:** `HomeCommand`, `HomesCommand`, `SetHomeCommand`, `HomeRemoveSubCommand`.

**API classes:** none found.

**Services:** none found.

**UI documents:** `Common/UI/Custom/Homes/Homes.ui`.

## EconomyPlugin

Maven: `com.hytalecity:EconomyPlugin:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`).

Optional dependencies: none declared.

**Command classes:** `MoneyCommand`, `MoneyAddSubCommand`, `MoneyRemoveSubCommand`, `MoneySendSubCommand`, `MoneySetSubCommand`.

**API classes:** none found.

**Services:** none found.

**UI documents:** none found.

## JobsPlugin

Maven: `com.hytalecity:JobsPlugin:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`), `HytaleCity:HcNpcs` (`*`).

Optional dependencies: `HytaleCity:EnchantmentsPlugin` (`*`).

**Command classes:** `JobCommand`, `JobAdminItemAddSubCommand`, `JobAdminMilestonesUiSubCommand`, `JobAdminNpcSetSubCommand`, `JobAdminShopUiSubCommand`, `JobAdminSubCommand`, `JobAdminUpgradeUiSubCommand`, `JobEnterSubCommand`, `JobInfoSubCommand`, `JobSellSubCommand`.

**API classes:** `JobsAPI`, `JobUpdateListener`.

**Services:** `EnchantmentsBridgeService`, `JobMilestoneRuntimeService`, `JobShopOfferService`, `JobUpgradeRecipeService`, `NpcJobKeyService`.

**UI documents:** `Common/UI/Custom/Jobs/JobMilestonePanel.ui`, `Common/UI/Custom/Jobs/JobNpc.ui`, `Common/UI/Custom/Jobs/JobShopAdmin.ui`, `Common/UI/Custom/Jobs/JobUpgradeAdmin.ui`, `Common/UI/Custom/Jobs/JobUpgradeSelect.ui`, `Common/UI/Custom/Jobs/Jobs.ui`, `Common/UI/Custom/Jobs/MilestoneAdmin.ui`, `Common/UI/Custom/Jobs/MilestoneRow.ui`, `Common/UI/Custom/Jobs/Profession.ui`, `Common/UI/Custom/Jobs/ProfessionCard.ui`, `Common/UI/Custom/Jobs/ProfessionTradeRow.ui`.

## LevelPlugin

Maven: `com.hytalecity:LevelPlugin:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`).

Optional dependencies: none declared.

**Command classes:** none found.

**API classes:** none found.

**Services:** `LevelService`.

**UI documents:** none found.

## HcNpcs

Maven: `com.hytalecity:HcNpcs:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`).

Optional dependencies: none declared.

**Command classes:** `NpcCommand`.

**API classes:** `HcNpcsAPI`, `HcNpcsService`, `NpcActionHandler`, `Registration`.

**Services:** `HcNpcsService`.

**UI documents:** `Common/UI/Custom/HcNpcs/ActionRow.ui`, `Common/UI/Custom/HcNpcs/Actions.ui`.

## EnchantmentsPlugin

Maven: `com.hytalecity:EnchantmentsPlugin:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`).

Optional dependencies: none declared.

**Command classes:** `EnchantItemCommand`.

**API classes:** `EnchantmentsApi`.

**Services:** `EnchantmentBehaviorService`, `EnchantmentsService`, `EnchantmentValueService`, `ItemUpgradeRollService`, `MoneyFindRewardService`.

**UI documents:** none found.

## PlayerStatsPlugin

Maven: `com.hytalecity:PlayerStatsPlugin:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`).

Optional dependencies: none declared.

**Command classes:** none found.

**API classes:** none found.

**Services:** none found.

**UI documents:** none found.

## PlayerHudPlugin

Maven: `com.hytalecity:PlayerHudPlugin:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`).

Optional dependencies: none declared.

**Command classes:** `HudCommand`.

**API classes:** none found.

**Services:** `HudService`.

**UI documents:** `Common/UI/Custom/Hud/PlayerHud.ui`.

## AfkPlugin

Maven: `com.hytalecity:AfkPlugin:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`).

Optional dependencies: none declared.

**Command classes:** none found.

**API classes:** none found.

**Services:** `AfkDisconnectService`, `AfkService`.

**UI documents:** none found.

## TeleportPlugin

Maven: `com.hytalecity:TeleportPlugin:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`).

Optional dependencies: none declared.

**Command classes:** `TpAcceptCommand`, `TpaCommand`, `TpDenyCommand`.

**API classes:** none found.

**Services:** `TpaService`.

**UI documents:** none found.

## WarpPlugin

Maven: `com.hytalecity:WarpPlugin:1.0.0`.

Required dependencies: none declared.

Optional dependencies: none declared.

**Command classes:** `CitySubCommand`, `FarmWorldSubCommand`, `SpawnSubCommand`, `WarpCommand`.

**API classes:** none found.

**Services:** none found.

**UI documents:** none found.

## FarmWorldPlugin

Maven: `com.hytalecity:FarmWorldPlugin:1.0.0`.

Required dependencies: none declared.

Optional dependencies: none declared.

**Command classes:** none found.

**API classes:** none found.

**Services:** `FarmWorldService`.

**UI documents:** none found.

## ProtectionPlugin

Maven: `com.hytalecity:ProtectionPlugin:1.0.0`.

Required dependencies: `HytaleCity:CorePlugin` (`*`).

Optional dependencies: none declared.

**Command classes:** `ProtectionCommand`, `ListSubCommand`, `RegisterSubCommand`, `RemoveSubCommand`.

**API classes:** none found.

**Services:** none found.

**UI documents:** none found.

## DocumentationPlugin

Maven: `com.hytalecity:DocumentationPlugin:1.0.0`.

Required dependencies: none declared.

Optional dependencies: none declared.

**Command classes:** `RulesCommand`, `TutorialCommand`.

**API classes:** none found.

**Services:** `DocumentationService`.

**UI documents:** `Common/UI/Custom/Rules/Rules.ui`, `Common/UI/Custom/Tutorial/Tutorial.ui`.
