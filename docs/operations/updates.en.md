# Updates and recovery

## Before replacing plugins

Check versions and manifest dependencies. Keep Core, HcNpcs, and Jobs on compatible versions. Back up the database and affected world and configuration files, then verify that the backups can be restored.

On a test server, check startup, schema changes, migration, NPCs, sales, and UIs. Deploy the same built JARs after validation. Compare checksums to confirm that the copied JARs match.

## Migrations

- General player levels are imported from legacy JSON through Core. The database then becomes the source of truth.
- Job NPCs are imported from `jobs_npc_job_keys` into Core definitions and actions. Existing definitions take precedence, including deliberately reset mappings.
- The schema adds `player_jobs.version` with a default of `0` for existing data.

Disable the NPC definition or remove the specific action to turn it off. Deleting the definition can allow a legacy assignment to reappear on import.

## Open sales

| State | Meaning and action |
| --- | --- |
| `PREPARED` | Removal may have occurred. Check the inventory plan and actual stacks. |
| `COMMITTED` | The database has applied the rewards. Do not refund automatically. |
| `REFUND_DUE` | Refund is pending or may be partial. Reconcile what was actually returned. |
| `ABORTED` | No payout is outstanding and the refund or absence of removal is confirmed. |

Use `JobSaleService.pending`, `diagnostic`, `commit`, `abort`, and `confirmRefund` for reconciliation. Confirm a refund after returning the items or verifying that no removal took place. A repeated `abort` does not authorize a second physical refund.

Inventory and world files cannot commit atomically with MariaDB. After an ambiguous interruption, check the operation ID before returning any items. See the [full contract](../reference/npc-contracts.md).
