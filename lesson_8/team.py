from . import database


def repr_players():
    team: dict[int, dict] = database.get_team()
    for number, player in team.items():
        print(f"\t[Player {number}]: {player['name']}, {player["age"]}")


def player_add(name: str, age: int, number: int) -> dict | None:
    player: dict = {"name": name, "age": age}
    saved: bool = database.save(id_=number, instance=player)  # can add "debug=True"

    if not saved:
        raise Exception(f"player# {number} already exists")
    else:
        return player


def player_update(name: str, age: int, number: int) -> dict | None:
    player: dict | None = database.get(id_=number)
    if player is not None:
        player["name"] = name
        player["age"] = age
        database.update(id_=number, instance=player)
        return player
    else:
        raise Exception(f"player with #{number} doesn't exist")
        return None


def player_delete(number: int) -> bool:
    team: dict[int, dict] = database.get_team()
    if not team.get(number):
        return False
    else:
        database.delete(id_=number)
        return True


def commands_commander(operation: str):
    operations: tuple[str, ...] = ("add", "del", "repr", "upd", "exit")
    if operation not in operations:
        raise Exception(f"Operation {operation}, is not available\n")

    if operation == "exit":
        raise SystemExit("Exiting the app")

    elif operation == "repr":
        repr_players()

    elif operation == "add":
        user_data = input("Enter the new player information [name, age, number]: ")
        user_items: list[str] = user_data.split(",")
        name, age, number = user_items
        try:
            player_add(name=name, age=int(age), number=int(number))
        except ValueError:
            raise Exception("Age and number must be integers\n\n")

    elif operation == "upd":
        user_data = input("Enter a new player's info [name, age, number]: ")
        user_items: list[str] = user_data.split(",")
        name, age, number = user_items
        try:
            new_player = player_update(name=name, age=int(age), number=int(number))
        except ValueError:
            raise Exception("Age and number must be integers\n\n")
        else:
            if new_player is None:
                raise Exception(f"player# {number} is not updated")
            else:
                print(
                    f"player [{number}] has been updated."
                    f"Name:[{new_player['name']}],"
                    f"age:[{new_player['age']}]"
                )

    elif operation == "del":
        user_data = input("Enter the palyer's # [int]: ")
        try:
            _user_data = int(user_data)
        except ValueError:
            raise Exception("player's# must be an integer")
        else:
            player_delete(number=_user_data)


def main():

    while True:
        operation = input("Please enter the operation: ")
        try:
            commands_commander(operation)
        except SystemExit as error:
            raise error
        except Exception as error:
            print(error)
            continue


if __name__ == "__main__":
    main()
