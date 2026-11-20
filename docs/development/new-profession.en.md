# Adding a profession

A new profession needs Java registration, database content, and a merchant. This example adds `Steinmetz` and reuses the mining event path.

## 1. Register the profession and NPC type

1. Add `STEINMETZ` with the stable key `Steinmetz` to Core's `JobType`.
2. Extend Core's `NpcJobBinding` in both directions for NPC type `steinmetz`. `typeKey` normalizes it to `typ:steinmetz`, and `jobKey` returns `Steinmetz`. Update error messages and mapping tests.
3. Register the key in Jobs' `JobKeyUtil` and check the commands and admin profession pickers. Add the visible name and activity hint to `ProfessionUI`. HcNpcs uses the Core mapping to pass the type to `job:merchant`. The NPC keeps its native Hytale role.
4. For a new XP source, connect it to `ProfessionActivities` through the corresponding successful server event. Award XP via `ProfessionService.activity`. For stone mining, the existing `BREAK` path must recognize the relevant rock block IDs for both mining and placement tracking.

Both `job_activity_rules` and `job_collection_rules` use a unique key consisting of the activity and target. Use a distinct block ID or decide which existing mapping to replace.

## 2. Add profession content through a migration

Add a numbered SQL migration to the Core changelog. This example uses `Rock_Basalt` and `Rock_Basalt_Cobble`.

~~~sql
INSERT INTO items (itemKey, jobKey, rarity, price, enabled)
VALUES ('Rock_Basalt_Cobble', 'Steinmetz', 'Gewöhnlich', 2, TRUE);

INSERT INTO job_activity_rules (activity, target_key, job_key, xp)
VALUES ('BREAK', 'Rock_Basalt', 'Steinmetz', 2);

INSERT INTO job_collection_rules (activity, target_key, job_key, item_key)
VALUES ('BREAK', 'Rock_Basalt', 'Steinmetz', 'Rock_Basalt_Cobble');

INSERT INTO job_merchant_stock
    (job_key, item_key, unit_price, capacity, refill_per_day, quantity)
VALUES ('Steinmetz', 'Rock_Basalt_Cobble', 5, 64, 32, 64);

INSERT INTO job_level_milestones (job_key, required_level, reward_money)
VALUES ('Steinmetz', 5, 100);

INSERT INTO job_milestone_definitions
    (jobKey, itemKey, amount, orderIndex, rewardMoney, rewardExp)
VALUES ('Steinmetz', 'Rock_Basalt_Cobble', 25, 0, 100, 20);
~~~

Item IDs are unique in `items`. Reassigning an item from another profession changes that profession's assortment and possibly its collection view. Stock in `job_merchant_stock` is shared for each profession and item. This example starts with 64.

Add level milestones at 10, 25, 50, 100, 150, 200, 500, and 1000, more collection tiers, and starter quests. This example offers three quests from level 1.

~~~sql
INSERT INTO job_quest_templates
    (quest_key, job_key, title, min_level, reward_money, reward_xp, enabled)
VALUES
    ('stone_basalt_break', 'Steinmetz', 'Arbeit im Steinbruch', 1, 30, 20, TRUE),
    ('stone_basalt_delivery', 'Steinmetz', 'Basaltlieferung', 1, 36, 20, TRUE),
    ('stone_basalt_both', 'Steinmetz', 'Basalt aus eigener Arbeit', 1, 40, 25, TRUE);

INSERT INTO job_quest_goals (quest_key, goal_type, target_key, goal_amount)
VALUES
    ('stone_basalt_break', 'BREAK', 'Rock_Basalt', 12),
    ('stone_basalt_delivery', 'DELIVER', 'Rock_Basalt_Cobble', 12),
    ('stone_basalt_both', 'BREAK', 'Rock_Basalt', 8),
    ('stone_basalt_both', 'DELIVER', 'Rock_Basalt_Cobble', 12);
~~~

The [quest and reward guide](../operations/profession-content.md) covers other goal types and rotation. Put level item rewards in `job_level_milestone_items`. Action goals need matching XP rules. Collection rules update milestone counters.

## 3. Build, bind the merchant, and verify

1. Build Core, HcNpcs, Jobs, and PlayerHud against the updated Core. Start with a test database and verify the migration.
2. Target an existing NPC and run `/hcnpc set merchant steinmetz`. Alternatively, use `/hcnpc set [identifier] merchant steinmetz`. See the [NPC guide](../plugins/npcs.md) for targeting and display names.
3. Open the merchant and activate the profession. Check HUD level and XP, stock, and daily quests. Switch professions and switch back while a quest is open.
4. Check XP and collection totals with naturally generated material. Then place and break a matching block. Breaking placed blocks, dropping, picking up, or selling items must leave the collection count unchanged.
5. Complete a quest and claim a collection and a level reward. Test claiming an item reward with a full inventory and retrying a claimed reward.
