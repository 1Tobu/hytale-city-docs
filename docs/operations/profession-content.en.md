# Creating profession quests and rewards

These examples use the MariaDB Core database with migrations V4 through V7 applied. Try the steps on a test server first. For rollout to multiple servers, put the SQL in a new Core Liquibase migration so the existing checksums stay intact.

## Add a quest

1. Choose a profession and a unique quest ID. The four profession keys are `Farmer`, `Holzfäller`, `Miner`, and `Jäger`.
2. Set the title, minimum level, money, and positive profession XP in `job_quest_templates`.
3. Add at least one goal in `job_quest_goals`. The example counts six gold ore blocks in basalt mined by the player and also requires delivery of four pieces of gold ore.
4. Open the merchant with an active Miner profession at level 10 or above. For a quick test, use a fresh test profile or wait for the next daily rotation. Whether the new template appears depends on that day's selection.

~~~sql
START TRANSACTION;

INSERT INTO job_quest_templates
    (quest_key, job_key, title, min_level, reward_money, reward_xp, enabled)
VALUES
    ('mine_basalt_gold', 'Miner', 'Gold aus dem Basalt', 10, 160, 40, TRUE);

INSERT INTO job_quest_goals (quest_key, goal_type, target_key, goal_amount)
VALUES
    ('mine_basalt_gold', 'BREAK', 'Ore_Gold_Basalt', 6),
    ('mine_basalt_gold', 'DELIVER', 'Ore_Gold', 4);

COMMIT;
~~~

| Goal type | `target_key` | When it counts |
|---|---|---|
| `DELIVER` | Inventory item ID such as `Ore_Gold` or a [custom item](../reference/custom-assets.md) | The quantity is taken from the player's inventory on delivery. |
| `BREAK` | Block ID such as `Ore_Gold_Basalt` | The matching natural block is successfully mined after accepting the quest. |
| `HARVEST` | Base plant ID such as `Plant_Crop_Carrot_Block` | A mature plant is harvested after accepting the quest. |
| `HUNT` | NPC role such as `Boar` | An eligible wild animal is killed after accepting the quest. |

For action goals, an asterisk matches all eligible activities of the profession. Progress requires a matching rule in `job_activity_rules`. A collection rule in `job_collection_rules` alone is insufficient. Every goal must be met in full. Deliveries can also come from stored goods or player trades.

The merchant stores up to three offers per player and profession per calendar day in Europe/Berlin. Two quests can be open at once. The active profession determines eligibility for acceptance, action progress, and delivery. Open quests survive both profession changes and daily rotations. Titles, goals, and rewards are copied at acceptance, so changes to a template affect future acceptances. Set `enabled` to `FALSE` to remove a template from rotation while keeping existing quests playable.

## Change a level milestone reward

The merchant's level milestones screen lets players claim each reached milestone once. `job_level_milestones` sets the money amount. `job_level_milestone_items` adds item IDs and quantities. The example sets a cash reward and two Vibranium bars for Miner level 25.

~~~sql
START TRANSACTION;

INSERT INTO job_level_milestones (job_key, required_level, reward_money)
VALUES ('Miner', 25, 1500)
ON DUPLICATE KEY UPDATE reward_money=VALUES(reward_money);

INSERT INTO job_level_milestone_items (job_key, required_level, item_key, quantity)
VALUES ('Miner', 25, 'HC_Ingredient_Bar_Vibranium', 2)
ON DUPLICATE KEY UPDATE quantity=VALUES(quantity);

COMMIT;
~~~

If needed, delete the old item row for the same profession and level using its old item ID. Set the money amount to zero for an item-only reward. Check the ID against the installed pack and test claiming with a full inventory, then with free space. Previously claimed milestones stay claimed when you edit rewards. Claims are recorded in `job_level_milestone_awards`.

## Change a collection milestone reward

1. Run `/job admin milestones` with an admin account.
2. Select a profession and item. Enter the required collection quantity, money, profession XP, and any item rewards.
3. Separate multiple item rewards with commas. `HC_Ingredient_Bar_Vibranium:2` grants two bars. Omitting the quantity grants one.
4. Save and verify the row on the merchant's collection milestones screen or with `/job info`. Test the claim with a separate test profile.

Collection definitions live in `job_milestone_definitions`, progress in `player_job_item_totals`, and claims in `player_job_milestone_claims`. To add a collection item, map the server-side action to its item ID through `job_collection_rules` and enable the item for that profession in `items`. Edit live milestones with care because changes to quantities, order, or selection can affect the claim key.
