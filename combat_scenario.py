import random
import gameplay_functions


def resting_animation(player, enemy, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite, barrier_active,
                      sharp_sense_active, in_battle, in_npc_interaction, graphics):

    if player.race == "amuna":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_amuna_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_amuna_battle"])
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_fighter_amuna_battle"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_amuna_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_amuna_battle"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_amuna_battle"])
    if player.race == "sorae":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_sorae_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_sorae_battle"])
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_fighter_sorae_battle"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_sorae_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sorae_battle"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_sorae_battle"])
    if player.race == "nuldar":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_nuldar_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_nuldar_battle"])
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_fighter_nuldar_battle"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_nuldar_battle"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_nuldar_battle"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_nuldar_battle"])

    if in_battle and not in_npc_interaction:
        if enemy.kind == "snake":
            snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                       snake_battle_sprite.y_coordinate,
                                       graphics["snake_battle"])
        if enemy.kind == "ghoul":
            ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                       ghoul_battle_sprite.y_coordinate,
                                       graphics["ghoul_battle"])


# update player character and enemy sprites for combat animation
def combat_animation(player, enemy, player_battle_sprite, snake_battle_sprite, ghoul_battle_sprite,
                     barrier_active, sharp_sense_active, hard_strike, graphics):
    # update player character sprite for combat animation
    if player.race == "amuna":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_amuna_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_amuna_attack"])
        if player.role == "fighter":
            if not hard_strike:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_fighter_amuna_attack"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_amuna_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_amuna_attack"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_amuna_attack"])
    if player.race == "sorae":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_sorae_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_sorae_attack"])
        if player.role == "fighter":
            if not hard_strike:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_fighter_sorae_attack"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_sorae_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sorae_attack"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_sorae_attack"])
    if player.race == "nuldar":
        if player.role == "mage":
            if barrier_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_barrier_nuldar_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_mage_nuldar_attack"])
        if player.role == "fighter":
            if not hard_strike:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_fighter_nuldar_attack"])
        if player.role == "scout":
            if sharp_sense_active:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_sense_nuldar_attack"])
            else:
                player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                            player_battle_sprite.y_coordinate,
                                            graphics["player_scout_nuldar_attack"])
        if player.role == "":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        graphics["player_no_role_nuldar_attack"])
    if enemy.kind == "snake":
        snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                   snake_battle_sprite.y_coordinate,
                                   graphics["snake_attack"])
    if enemy.kind == "ghoul":
        ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                   ghoul_battle_sprite.y_coordinate,
                                   graphics["ghoul_attack"])


def fighter(player, player_battle_sprite, current_enemy_battling, snake_battle_sprite,
            ghoul_battle_sprite, player_fighter_amuna_strike, player_fighter_sorae_strike,
            player_fighter_nuldar_strike, snake_attack, ghoul_attack):

    # update animations for hard strike attack
    if player.race == "amuna":
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        player_fighter_amuna_strike)
    if player.race == "sorae":
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        player_fighter_sorae_strike)
    if player.race == "nuldar":
        if player.role == "fighter":
            player_battle_sprite.update(player_battle_sprite.x_coordinate,
                                        player_battle_sprite.y_coordinate,
                                        player_fighter_nuldar_strike)

    if current_enemy_battling.kind == "snake":
        snake_battle_sprite.update(snake_battle_sprite.x_coordinate,
                                   snake_battle_sprite.y_coordinate,
                                   snake_attack)
    if current_enemy_battling.kind == "ghoul":
        ghoul_battle_sprite.update(ghoul_battle_sprite.x_coordinate,
                                   ghoul_battle_sprite.y_coordinate,
                                   ghoul_attack)


def enemy_health_bar(enemys, graphics):
    try:
        enemys.health_bar.update(enemys.health_bar.x_coordinate, enemys.health_bar.y_coordinate,
                                 gameplay_functions.health_bar_update(enemys, graphics))
    except AttributeError:
        pass


def attack_scenario(enemy_combating, combat_event, player, level_up_win, level_up_font, hard_strike_learned,
                    graphics):
    # get the all the stuff that happened in this scenario and return it to main loop via dictionary keys and values
    combat_event_dictionary = {
        "damage done string": 0, "damage taken string": 0, "damage done": 0, "damage taken": 0,
        "item dropped": "", "experience gained": 0, "quest update": "", "enemy defeated": False,
        "level up status": "", "level up attributes": ""
    }
    if combat_event == "attack":
        if enemy_combating.alive_status:
            # returns players damage to the enemy based on level and equipment
            damage_to_enemy = gameplay_functions.attack_enemy(player, enemy_combating)
            enemy_combating.health = enemy_combating.health - damage_to_enemy
            enemy_health_bar(enemy_combating, graphics)

            # if enemy is not dead yet
            if enemy_combating.health > 0:
                attacked_enemy_string = f" You did {damage_to_enemy} damage to {enemy_combating.name}."
                combat_event_dictionary["damage done"] = damage_to_enemy
                # add damage to enemy to event dictionary to be returned to main loop
                combat_event_dictionary["damage done string"] = attacked_enemy_string
                # returns total damage output from enemy as attacked_player_health value
                damage_to_player = gameplay_functions.attack_player(player, enemy_combating)
                if damage_to_player > 0:
                    attacked_player_string = f"You take {damage_to_player} damage from {enemy_combating.name}."
                    player.health = player.health - damage_to_player
                    combat_event_dictionary["damage taken"] = damage_to_player
                    # add damage done to player from enemy to dictionary
                    combat_event_dictionary["damage taken string"] = attacked_player_string

                    # player health is less than or equal to 0, player is dead
                    if player.health <= 0:
                        player.alive_status = False
                    return combat_event_dictionary
                else:
                    enemy_miss_string = f'{enemy_combating.name} missed.'
                    # add to dictionary that enemy did no damage to player
                    combat_event_dictionary["damage taken string"] = enemy_miss_string
                    return combat_event_dictionary

            # enemy has been defeated, will return an amount of xp based on current levels
            else:
                # if player is on quest to kill snakes
                if enemy_combating.kind == "snake":
                    if player.quest_status["sneaky snakes"]:
                        if player.quest_progress["sneaky snakes"] < 4:
                            player.quest_progress["sneaky snakes"] = player.quest_progress["sneaky snakes"] + 1
                            quest_string = f"{player.quest_progress['sneaky snakes']}/4 snakes"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # if player is on quest to kill ghouls
                if enemy_combating.kind == "ghoul":
                    if player.quest_status["ghouled again"]:
                        if player.quest_progress["ghouled again"] < 4:
                            player.quest_progress["ghouled again"] = player.quest_progress["ghouled again"] + 1
                            quest_string = f"{player.quest_status['ghouled again']}/4 ghouls"
                            combat_event_dictionary["quest update"] = quest_string
                else:
                    combat_event_dictionary["quest update"] = "No"

                # experienced gained by player from defeating enemy
                if player.level <= enemy_combating.level + 1:
                    experience = int((enemy_combating.level / player.level) * 30)
                    player.experience = player.experience + experience
                    enemy_experience = f"{experience}"
                    # add to dictionary experience given from defeating enemy
                    combat_event_dictionary["experience gained"] = enemy_experience
                # player gains less experience if they're 1 level higher or more than enemy
                if player.level > enemy_combating.level + 1:
                    experience = int((enemy_combating.level / player.level))
                    player.experience = player.experience + experience
                    enemy_experience = f"{experience}"
                    # add to dictionary experience given from defeating enemy
                    combat_event_dictionary["experience gained"] = enemy_experience

                drop_chance = random.randrange(1, 10)
                # 80% chance (roughly?) to drop merchant item sellable by player for rupees at shops
                if drop_chance > 2:

                    # doesn't give item to player if their inventory is full
                    if len(player.items) < 16:
                        player.items.append(enemy_combating.items)
                        enemy_dropped_this = f"{enemy_combating.name} dropped [{enemy_combating.items.name}]."
                        # add to dictionary anything dropped from enemy upon their defeat
                        combat_event_dictionary["item dropped"] = enemy_dropped_this
                    else:
                        combat_event_dictionary["item dropped"] = "Item, but your inventory is full."
                else:
                    combat_event_dictionary["item dropped"] = "No"

                # player will level up if experience greater than or equal to 100
                if player.experience >= 100:
                    gameplay_functions.level_up(player, level_up_win, level_up_font)

                enemy_combating.alive_status = False
                enemy_combating.kill()

                # add to dictionary True if enemy has been defeated
                combat_event_dictionary["enemy defeated"] = True
                return combat_event_dictionary

    # active combat skill, if player is fighter and has learned hard strike from the academia
    # same as default attack from above, but attack replaced by hard strike skill
    if combat_event == "skill 1":
        if player.role == "fighter":
            if hard_strike_learned:
                if enemy_combating.alive_status:
                    striked = random.randrange(25, 35)  # hard strike damage
                    enemy_combating.health = enemy_combating.health - striked
                    enemy_health_bar(enemy_combating, graphics)
                    if enemy_combating.health > 0:
                        attacked_enemy_string = f"Hard strike did {striked} damage!"
                        combat_event_dictionary["damage done"] = striked
                        combat_event_dictionary["damage done string"] = attacked_enemy_string
                        damage_to_player = gameplay_functions.attack_player(player, enemy_combating)
                        if damage_to_player > 0:
                            attacked_player_string = f"You take {damage_to_player} damage from " \
                                                     f"{enemy_combating.name}."
                            player.health = player.health - damage_to_player
                            combat_event_dictionary["damage taken"] = damage_to_player
                            combat_event_dictionary["damage taken string"] = attacked_player_string
                            if player.health <= 0:
                                player.alive_status = False
                            return combat_event_dictionary
                        else:
                            enemy_miss_string = f'{enemy_combating.name} missed.'
                            combat_event_dictionary["damage taken string"] = enemy_miss_string
                            return combat_event_dictionary
                    else:
                        if enemy_combating.kind == "snake":
                            if player.quest_status["sneaky snakes"]:
                                if player.quest_progress["sneaky snakes"] < 4:
                                    player.quest_progress["sneaky snakes"] = player.quest_progress["sneaky snakes"] + 1
                                    quest_string = f"{player.quest_progress['sneaky snakes']}/4 snakes"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"
                        if enemy_combating.kind == "ghoul":
                            if player.quest_status["ghouled again"]:
                                if player.quest_progress["ghouled again"] < 4:
                                    player.quest_progress["ghouled again"] = player.quest_progress["ghouled again"] + 1
                                    quest_string = f"{player.quest_status['ghouled again']}/4 ghouls"
                                    combat_event_dictionary["quest update"] = quest_string
                        else:
                            combat_event_dictionary["quest update"] = "No"
                        # experienced gained by player from defeating enemy
                        if player.level <= enemy_combating.level + 1:
                            experience = int((enemy_combating.level / player.level) * 30)
                            player.experience = player.experience + experience
                            enemy_experience = f"{experience}"
                            # add to dictionary experience given from defeating enemy
                            combat_event_dictionary["experience gained"] = enemy_experience
                        # player gains less experience if they're 1 level higher or more than enemy
                        if player.level > enemy_combating.level + 1:
                            experience = int((enemy_combating.level / player.level))
                            player.experience = player.experience + experience
                            enemy_experience = f"{experience}"
                            # add to dictionary experience given from defeating enemy
                            combat_event_dictionary["experience gained"] = enemy_experience
                        drop_chance = random.randrange(1, 10)
                        if drop_chance > 2:
                            if len(player.items) < 16:
                                player.items.append(enemy_combating.items)
                                enemy_dropped_this = f"{enemy_combating.name} dropped [{enemy_combating.items.name}]."
                                combat_event_dictionary["item dropped"] = enemy_dropped_this
                            else:
                                combat_event_dictionary["item dropped"] = "Item, but your inventory is full."
                        else:
                            combat_event_dictionary["item dropped"] = "No"
                        if player.experience >= 100:
                            gameplay_functions.level_up(player, level_up_win, level_up_font)
                        enemy_combating.alive_status = False
                        enemy_combating.kill()
                        combat_event_dictionary["enemy defeated"] = True
                        return combat_event_dictionary