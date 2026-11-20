# Custom assets

The shared **HytaleCity:Assets** pack is in [hytale-city-assets](https://github.com/1Tobu/hytale-city-assets). Install **HytaleCity.Assets** in the server's asset pack or mods directory. When installing from a ZIP, place the manifest at the root of the archive. On update, replace the previous pack and restart the server.

**Item IDs** are the filenames under `Server/Item/Items` without the `.json` extension. Use them with `/give`, quest deliveries, and reward lists. Block sets, hitboxes, and particles have their own asset types. Models, textures, icons, and UI documents are referenced by resource path.

Core supports the [migration to HC_ IDs](../operations/database-migrations.md#asset-migration) for known database references. Check existing items and blocks in world data separately. Mappings for former IDs and resource paths are in the pack's development directory.


This inventory is based on asset commit **07e129e** and contains all 85 versioned runtime files in the pack.

## Registered items and placeable blocks (23)

- [HC_Ingredient_Bar_Vibranium](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/HC_Ingredient_Bar_Vibranium.json)
- [HC_Portal_To_Arena](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/HC_Portal_To_Arena.json)
- [HC_Portal_To_City](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/HC_Portal_To_City.json)
- [HC_Portal_To_Farmworld](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/HC_Portal_To_Farmworld.json)
- [HC_Spawn_Portal_To_City](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/HC_Spawn_Portal_To_City.json)
- [HC_Ore_Vibranium](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Ore/Vibranium/HC_Ore_Vibranium.json)
- [HC_Tool_Hatchet_Vibranium](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Hatchet/HC_Tool_Hatchet_Vibranium.json)
- [HC_Tool_Hatchet_VibraniumV2](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Hatchet/HC_Tool_Hatchet_VibraniumV2.json)
- [HC_Tool_Hatchet_VibraniumV3](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Hatchet/HC_Tool_Hatchet_VibraniumV3.json)
- [HC_Tool_Hatchet_VibraniumV4](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Hatchet/HC_Tool_Hatchet_VibraniumV4.json)
- [HC_Tool_Hoe_Vibranium](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Hoe/HC_Tool_Hoe_Vibranium.json)
- [HC_Tool_Hoe_VibraniumV2](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Hoe/HC_Tool_Hoe_VibraniumV2.json)
- [HC_Tool_Hoe_VibraniumV3](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Hoe/HC_Tool_Hoe_VibraniumV3.json)
- [HC_Tool_Hoe_VibraniumV4](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Hoe/HC_Tool_Hoe_VibraniumV4.json)
- [HC_Tool_Pickaxe_Vibranium](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Pickaxe/HC_Tool_Pickaxe_Vibranium.json)
- [HC_Tool_Pickaxe_VibraniumV2](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Pickaxe/HC_Tool_Pickaxe_VibraniumV2.json)
- [HC_Tool_Pickaxe_VibraniumV3](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Pickaxe/HC_Tool_Pickaxe_VibraniumV3.json)
- [HC_Tool_Pickaxe_VibraniumV4](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Tools/Pickaxe/HC_Tool_Pickaxe_VibraniumV4.json)
- [HC_Wand_Aegis](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Weapons/Wand/HC_Wand_Aegis.json)
- [HC_Wand_Astral](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Weapons/Wand/HC_Wand_Astral.json)
- [HC_Wand_Ember](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Weapons/Wand/HC_Wand_Ember.json)
- [HC_Wand_Frost](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Weapons/Wand/HC_Wand_Frost.json)
- [HC_Wand_Verdant](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Items/Weapons/Wand/HC_Wand_Verdant.json)

## Other server assets and manifest

- [Server/Item/Block/Hitboxes/HC_Spawn_Portal_To_City_Hitbox.json](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Block/Hitboxes/HC_Spawn_Portal_To_City_Hitbox.json)
- [Server/Item/Block/Sets/HC_Ore_Vibranium.json](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Item/Block/Sets/HC_Ore_Vibranium.json)
- [Server/Languages/de-DE/server.lang](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Languages/de-DE/server.lang)
- [Server/Languages/en-US/server.lang](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Languages/en-US/server.lang)
- [Server/Particles/Block/Crystal/HC_Plot_Border_Particle.particlesystem](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Particles/Block/Crystal/HC_Plot_Border_Particle.particlesystem)
- [Server/Particles/Block/Crystal/Spawners/HC_Plot_Border_Particle_Color.particlespawner](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Server/Particles/Block/Crystal/Spawners/HC_Plot_Border_Particle_Color.particlespawner)
- [manifest.json](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/manifest.json)

## Models, textures, and icons

- [Common/Icons/Items/Resources/Ores/HC_Ore_Vibranium.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Resources/Ores/HC_Ore_Vibranium.png)
- [Common/Icons/Items/Tools/Hatchet/HC_Tool_Hatchet_Vibranium.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Hatchet/HC_Tool_Hatchet_Vibranium.png)
- [Common/Icons/Items/Tools/Hatchet/HC_Tool_Hatchet_VibraniumV2.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Hatchet/HC_Tool_Hatchet_VibraniumV2.png)
- [Common/Icons/Items/Tools/Hatchet/HC_Tool_Hatchet_VibraniumV3.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Hatchet/HC_Tool_Hatchet_VibraniumV3.png)
- [Common/Icons/Items/Tools/Hatchet/HC_Tool_Hatchet_VibraniumV4.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Hatchet/HC_Tool_Hatchet_VibraniumV4.png)
- [Common/Icons/Items/Tools/Hoe/HC_Tool_Hoe_Vibramium.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Hoe/HC_Tool_Hoe_Vibramium.png)
- [Common/Icons/Items/Tools/Hoe/HC_Tool_Hoe_VibramiumV2.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Hoe/HC_Tool_Hoe_VibramiumV2.png)
- [Common/Icons/Items/Tools/Hoe/HC_Tool_Hoe_VibraniumV2.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Hoe/HC_Tool_Hoe_VibraniumV2.png)
- [Common/Icons/Items/Tools/Hoe/HC_Tool_Hoe_VibraniumV3.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Hoe/HC_Tool_Hoe_VibraniumV3.png)
- [Common/Icons/Items/Tools/Hoe/HC_Tool_Hoe_VibraniumV4.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Hoe/HC_Tool_Hoe_VibraniumV4.png)
- [Common/Icons/Items/Tools/Pickaxe/HC_Tool_Pickaxe_VibraniumV1.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Pickaxe/HC_Tool_Pickaxe_VibraniumV1.png)
- [Common/Icons/Items/Tools/Pickaxe/HC_Tool_Pickaxe_VibraniumV2.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Pickaxe/HC_Tool_Pickaxe_VibraniumV2.png)
- [Common/Icons/Items/Tools/Pickaxe/HC_Tool_Pickaxe_VibraniumV3.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Pickaxe/HC_Tool_Pickaxe_VibraniumV3.png)
- [Common/Icons/Items/Tools/Pickaxe/HC_Tool_Pickaxe_VibraniumV4.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Tools/Pickaxe/HC_Tool_Pickaxe_VibraniumV4.png)
- [Common/Icons/Items/Weapons/Wand/HC_Wand_Aegis_Icon64.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Weapons/Wand/HC_Wand_Aegis_Icon64.png)
- [Common/Icons/Items/Weapons/Wand/HC_Wand_Astral_Icon64.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Weapons/Wand/HC_Wand_Astral_Icon64.png)
- [Common/Icons/Items/Weapons/Wand/HC_Wand_Ember_Icon64.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Weapons/Wand/HC_Wand_Ember_Icon64.png)
- [Common/Icons/Items/Weapons/Wand/HC_Wand_Frost_Icon64.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Weapons/Wand/HC_Wand_Frost_Icon64.png)
- [Common/Icons/Items/Weapons/Wand/HC_Wand_Verdant_Icon64.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Icons/Items/Weapons/Wand/HC_Wand_Verdant_Icon64.png)
- [Common/Items/Resources/Materials/Ingot_Textures/HC_Vibranium.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Resources/Materials/Ingot_Textures/HC_Vibranium.png)
- [Common/Items/Resources/Ores/Ores_Texture/HC_Vibranium.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Resources/Ores/Ores_Texture/HC_Vibranium.png)
- [Common/Items/Tools/Hatchet/HC_VibraniumV1_Hatchet_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hatchet/HC_VibraniumV1_Hatchet_Texture.png)
- [Common/Items/Tools/Hatchet/HC_VibraniumV2_Hatchet_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hatchet/HC_VibraniumV2_Hatchet_Texture.png)
- [Common/Items/Tools/Hatchet/HC_VibraniumV3_Hatchet_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hatchet/HC_VibraniumV3_Hatchet_Texture.png)
- [Common/Items/Tools/Hatchet/HC_VibraniumV4_Hatchet_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hatchet/HC_VibraniumV4_Hatchet_Texture.png)
- [Common/Items/Tools/Hatchet/HC_Vibranium_Hatchet_v1.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hatchet/HC_Vibranium_Hatchet_v1.blockymodel)
- [Common/Items/Tools/Hatchet/HC_Vibranium_Hatchet_v2.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hatchet/HC_Vibranium_Hatchet_v2.blockymodel)
- [Common/Items/Tools/Hatchet/HC_Vibranium_Hatchet_v3.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hatchet/HC_Vibranium_Hatchet_v3.blockymodel)
- [Common/Items/Tools/Hatchet/HC_Vibranium_Hatchet_v4.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hatchet/HC_Vibranium_Hatchet_v4.blockymodel)
- [Common/Items/Tools/Hoe/HC_VibraniumV2_Hoe_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hoe/HC_VibraniumV2_Hoe_Texture.png)
- [Common/Items/Tools/Hoe/HC_VibraniumV3_Hoe_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hoe/HC_VibraniumV3_Hoe_Texture.png)
- [Common/Items/Tools/Hoe/HC_VibraniumV4_Hoe_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hoe/HC_VibraniumV4_Hoe_Texture.png)
- [Common/Items/Tools/Hoe/HC_Vibranium_Hoe.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hoe/HC_Vibranium_Hoe.blockymodel)
- [Common/Items/Tools/Hoe/HC_Vibranium_Hoe_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hoe/HC_Vibranium_Hoe_Texture.png)
- [Common/Items/Tools/Hoe/HC_Vibranium_Hoe_v2.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hoe/HC_Vibranium_Hoe_v2.blockymodel)
- [Common/Items/Tools/Hoe/HC_Vibranium_Hoe_v3.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hoe/HC_Vibranium_Hoe_v3.blockymodel)
- [Common/Items/Tools/Hoe/HC_Vibranium_Hoe_v4.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Hoe/HC_Vibranium_Hoe_v4.blockymodel)
- [Common/Items/Tools/Pickaxe/HC_VibraniumV1_Pickaxe_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Pickaxe/HC_VibraniumV1_Pickaxe_Texture.png)
- [Common/Items/Tools/Pickaxe/HC_VibraniumV2_Pickaxe_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Pickaxe/HC_VibraniumV2_Pickaxe_Texture.png)
- [Common/Items/Tools/Pickaxe/HC_VibraniumV3_Pickaxe_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Pickaxe/HC_VibraniumV3_Pickaxe_Texture.png)
- [Common/Items/Tools/Pickaxe/HC_VibraniumV4_Pickaxe_Texture.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Pickaxe/HC_VibraniumV4_Pickaxe_Texture.png)
- [Common/Items/Tools/Pickaxe/HC_Vibranium_pickaxe_v1.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Pickaxe/HC_Vibranium_pickaxe_v1.blockymodel)
- [Common/Items/Tools/Pickaxe/HC_Vibranium_pickaxe_v2.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Pickaxe/HC_Vibranium_pickaxe_v2.blockymodel)
- [Common/Items/Tools/Pickaxe/HC_Vibranium_pickaxe_v3.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Pickaxe/HC_Vibranium_pickaxe_v3.blockymodel)
- [Common/Items/Tools/Pickaxe/HC_Vibranium_pickaxe_v4.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Tools/Pickaxe/HC_Vibranium_pickaxe_v4.blockymodel)
- [Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Aegis.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Aegis.blockymodel)
- [Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Aegis.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Aegis.png)
- [Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Astral.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Astral.blockymodel)
- [Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Astral.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Astral.png)
- [Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Ember.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Ember.blockymodel)
- [Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Ember.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Ember.png)
- [Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Frost.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Frost.blockymodel)
- [Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Frost.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Frost.png)
- [Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Verdant.blockymodel](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Verdant.blockymodel)
- [Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Verdant.png](https://github.com/1Tobu/hytale-city-assets/blob/07e129ef98123a570fe0c71d7aa229f4b2df58ec/HytaleCity.Assets/Common/Items/Weapons/Wand/HytaleCity/HC_Wand_Verdant.png)

## Plugin runtime assets

These Common and Server resources ship with their respective JARs. Mirrors under `assets/Common` are listed once.

### HcNpcs

- `Common/UI/Custom/HcNpcs/ActionRow.ui`
- `Common/UI/Custom/HcNpcs/Actions.ui`

### hytale-city-build-plugin

- `Common/UI/Custom/Plots/Plots.ui`

### hytale-city-documentation-plugin

- `Common/UI/Custom/Rules/Rules.ui`
- `Common/UI/Custom/Tutorial/HytaleCity.png`
- `Common/UI/Custom/Tutorial/Tutorial.ui`

### hytale-home-plugin

- `Common/UI/Custom/Homes/Homes.ui`

### hytale-jobs-plugin

- `Common/UI/Custom/Jobs/JobMilestonePanel.ui`
- `Common/UI/Custom/Jobs/JobNpc.ui`
- `Common/UI/Custom/Jobs/JobShopAdmin.ui`
- `Common/UI/Custom/Jobs/JobUpgradeAdmin.ui`
- `Common/UI/Custom/Jobs/JobUpgradeSelect.ui`
- `Common/UI/Custom/Jobs/Jobs.ui`
- `Common/UI/Custom/Jobs/MilestoneAdmin.ui`
- `Common/UI/Custom/Jobs/MilestoneRow.ui`
- `Common/UI/Custom/Jobs/Profession.ui`
- `Common/UI/Custom/Jobs/ProfessionCard.ui`
- `Common/UI/Custom/Jobs/ProfessionTradeRow.ui`

### hytale-playerhud-plugin

- `Common/UI/Custom/Hud/PlayerHud.ui`
- `Common/UI/Custom/Hud/PlayerHudPanel.png`
