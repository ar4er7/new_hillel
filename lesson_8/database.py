TEAM_TYPE = dict[int, dict]

_TEAM: TEAM_TYPE = {
    1: {"name":"John", "age": 20}, 
    3: {"name":"Mark", "age": 33},
    31: {"name":"Kevin", "age": 31}
}

def get_team() -> TEAM_TYPE:
    return _TEAM

def save(id_: int, instance: dict, debug:bool=False)-> bool:
    try:
        print(_TEAM[id_])
        if debug is True:
            print(f"the instance with id: {id_} already exists")
        return False
    except KeyError:  
        _TEAM[id_] = instance
        return True
    
def delete(id_:int, debug: bool=False) -> bool:
    try:
        del _TEAM[id_]
    except KeyError:
        if debug:
            print(f"there is no instance with #{id_}")
        return False
    else:
        return True