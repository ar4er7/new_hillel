from . import database

def repr_players(): 
    team: dict[int,dict] = database.get_team()
    for number, player in team.items():
        print(f"\t[Player {number}]: {player['name']}, {player["age"]}")

def player_add(name: str, age: int, number: int) -> dict | None:
    player: dict = {"name":name, "age":age}
    saved: bool = database.save(id_=number, instance=player) #can add "debug=True" 
    
    if not saved:
        print(f"player# {number} already exists")
    else:
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
        
            

def player_delete(number: int)-> bool:
    team: dict[int, dict] = database.get_team()
    if not team.get(number):
        return False
    else:
        database.delete(id_=number)
        return True


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
            repr_players()
            
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
        
        elif operation == "del":
            user_data = input("Enter the palyer's # [int]: ")
            try:
                _user_data = int(user_data)
            except ValueError:
                print("player's# must be an integer")
                continue
            else:
                player_delete(number=_user_data)

        else:
            raise NotImplementedError
    
if __name__ == "__main__":
    main()
    