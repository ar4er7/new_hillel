TEAM_TYPE = dict[int, dict]

class DatabaseError(Exception):
    pass

_TEAM: TEAM_TYPE = {
    1: {"name":"John", "age": 20}, 
    3: {"name":"Mark", "age": 33},
    31: {"name":"Kevin", "age": 31}
}

def get_team() -> TEAM_TYPE:
    return _TEAM

def get(id_: int) -> dict:
    try:
        player = _TEAM[id_]
    except KeyError:
        raise DatabaseError(f"id: {id_} doesn't exist")
    else:
        return player
    
def save(id_: int, instance: dict)-> dict:
    if _TEAM.get(id_) is not None:
        raise DatabaseError(f"the instance with id: {id_} already exists")
    else:
        _TEAM[id_] = instance
        return instance
    
def update(id_:int, instance: dict):
    _: dict = get(id_=id_)
    _TEAM[id_] = instance
    return instance
    
def delete(id_:int):
    _:dict = get(id_=id_)
    del _TEAM[id_]
