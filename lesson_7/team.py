

team: list[dict] = [
    {"name":"John", "age": 20, "number": 1}, 
    {"name":"Mark", "age": 33, "number": 3},
    {"name":"Kevin", "age": 31, "number": 12},
]

def repr_players(players: list[dict]):
    for player in players:
        print(
            f"\t[Player {player['number']}]: {player['name']}, {player["age"]}"
            )

def player_add(name: str, age: int, number: int) -> dict:
    for player in team:
        if player["number"] == number:
            print(f"the player with #{number} exists")
            break
        else:
            player: dict = {
                "name" : name,
                "age" : age,
                "number" : number, 
            }
            team.append(player)
            return player
        
def player_update(new_name: str, new_age: int, player_num:int)->None:
    is_found = False
    for player in team:
        if player["number"] == player_num:
            player["name"] = new_name
            player["age"] = new_age
            print(f"player# {player_num} new name {new_name}, new age {new_age}")
            is_found = True
                        
    if is_found == False:
        raise ValueError
        
            

def player_delete(number: int)-> None:
    for player in team:
        if player["number"] == number:
            del player

def main():    
    operations: tuple[str, ...] = ("add", "del", "repr", "upd", "exit")
    
    while True:
        operation = input("Please enter the operation: ")
        if operation not in operations:
            print(f"Operation {operation}, is not available\n")
            continue
        
        if operation == "exit":
            print("Bye")
            break
        elif operation == "repr":
            repr_players(team)
        elif operation == "add":
            user_data = input("Enter the new player information [name, age, number]: ")
            user_items: list[str] = user_data.split(",")
            name, age, number = user_items
            try:
                player_add(name=name, age=int(age), number=int(number))
            except ValueError:
                print("Age and number must be integers\n\n")
                continue
        elif operation == "upd":
            user_data = input("Enter a new name, age and# [name, age, number]: ")
            user_items: list[str] = user_data.split(",")
            name, age, num = user_items
            try:
                player_update(name, int(age), int(num))
            except:
                ValueError
                print(f"there is no player with # {num}")
                continue

        else:
            raise NotImplementedError
    
if __name__ == "__main__":
    main()
    