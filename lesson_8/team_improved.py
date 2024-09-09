from . import database_improved as database


def repr_players():
    team: dict[int, dict] = database.get_team()
    for number, player in team.items():
        print(f"\t[Player {number}]: {player['name']}, {player["age"]}")


def player_add(name: str, age: int, number: int) -> dict:
    player_data: dict = {"name": name, "age": age}
    created_player: dict = database.save(id_=number, instance=player_data)
    return created_player


def player_update(name: str, age: int, number: int) -> dict:
    player_data: dict = {"name": name, "age": age}
    updated_player: dict = database.update(id_=number, instance=player_data)
    return updated_player


def player_delete(number: int) -> None:
    database.delete(id_=number)


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
        player_add(name=name, age=int(age), number=int(number))
        print(f"player {number} added")

    elif operation == "upd":
        user_data = input("Enter a new player's info [name, age, number]: ")
        user_items: list[str] = user_data.split(",")
        name, age, number = user_items
        updated_player: dict = player_update(
            name=name, age=int(age), number=int(number)
        )

        print(
            f"player [{number}] has been updated."
            f"Name:[{updated_player['name']}],"
            f"age:[{updated_player['age']}]"
        )

    elif operation == "del":
        user_data = input("Enter the palyer's # [int]: ")
        try:
            number = int(user_data)
        except ValueError:
            raise Exception("player's# must be an integer")
        else:
            print(f"player# {number} has been deleted")
            player_delete(number=number)


def main():

    while True:
        operation = input("Please enter the operation: ")
        try:
            commands_commander(operation)
        except SystemExit as error:
            raise error
        except database.DatabaseError as error:
            print(error)
        except Exception as error:
            print(f"unexpected error: {error}")


if __name__ == "__main__":
    main()
