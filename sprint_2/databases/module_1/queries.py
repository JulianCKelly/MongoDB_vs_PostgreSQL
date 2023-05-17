'''Relevant queries for rpg'''

SELECT_ALL = QUERY = 'SELECT character_id,name FROM charactercreator_character;'

AVG_ITEM_WEIGHT_PER_CHARACTER = '''
SELECT cc_char.name, AVG(ai.weight) AS
avg_item_weight FROM
charactercreator_character AS cc_char
JOIN charactercreator_character_inventory AS cc_inv
ON cc_char.character_id=cc_inv.character_id
JOIN armory_item AS ai
ON ai.item_id = cc_inv.item_id
GROUP BY cc_char.character_id
'''

TOTAL_CHARACTERS = '''
    SELECT COUNT(*) FROM charactercreator_character
'''

DISTINCT_CHARACTER_NAMES = '''
    SELECT COUNT(DISTINCT name) AS distinct_naems
    FROM charactercreator_character;
'''

TOTAL_NECROMANCERS = '''SELECT COUNT(*) FROM charactercreator_necromancer'''

TOTAL_ARMORY_ITEMS = '''
    SELECT COUNT (*) FROM  armory_item;
'''

TOTAL_WEAPONS = '''
    SELECT COUNT(*)
    FROM armory_weapon AS aw
    INNER JOIN armory_item AS ai
    WHERE ai.item_id=aw.item_ptr_id;
'''


TOTAL_NON_WEAPONS = '''
    SELECT COUNT(*)
    FROM armory_item AS ai
    LEFT JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    WHERE aw.power IS NULL;
'''

ITEMS_PER_CHARACTER = '''
    SELECT name,COUNT(item_id)
    FROM charactercreator_character AS cc_char
    INNER JOIN charactercreator_character_inventory cc_inv
    ON cc_char.character_id = cc_inv.character_id
    GROUP BY cc_char.character_id
    LIMIT 20
'''

WEAPONS_PER_CHARACTER = '''
    SELECT cc_char.name, COUNT(ai.item_id) AS total_weapons
    FROM armory_item AS ai
    INNER JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    -- 37 weapons
    INNER JOIN charactercreator_character_inventory AS cc_inv
    ON ai.item_id = cc_inv.item_id
    -- 203 weapons
    INNER JOIN charactercreator_character AS cc_char
    ON cc_char.character_id = cc_inv.character_id
    GROUP BY cc_char.character_id
    LIMIT 20
'''

AVG_CHARACTER_ITEMS = '''
    SELECT AVG(total_items)AS average_items_per_character
    FROM(SELECT name,COUNT(item_id)AS total_items
    FROM charactercreator_character AS cc_char
    INNER JOIN charactercreator_character_inventory cc_inv
    ON cc_char.character_id = cc_inv.character_id
    GROUP BY cc_char.character_id)
'''

AVG_CHARACTER_WEAPONS = '''
    SELECT AVG(total_weapons) AS average_weapons
    FROM(SELECT cc_char.name, COUNT(ai.item_id) AS total_weapons
    FROM armory_item AS ai
    INNER JOIN armory_weapon AS aw
    ON ai.item_id = aw.item_ptr_id
    -- 37 weapons
    INNER JOIN charactercreator_character_inventory AS cc_inv
    ON ai.item_id = cc_inv.item_id
    -- 203 weapons
    INNER JOIN charactercreator_character AS cc_char
    ON cc_char.character_id = cc_inv.character_id
    GROUP BY cc_char.character_id
    LIMIT 20)'''

QUERY_LIST = [TOTAL_CHARACTERS,
              TOTAL_NECROMANCERS,
              DISTINCT_CHARACTER_NAMES,
              TOTAL_ARMORY_ITEMS,
              TOTAL_WEAPONS,
              TOTAL_NON_WEAPONS,
              ITEMS_PER_CHARACTER,
              WEAPONS_PER_CHARACTER,
              AVG_CHARACTER_ITEMS,
              AVG_CHARACTER_WEAPONS]
