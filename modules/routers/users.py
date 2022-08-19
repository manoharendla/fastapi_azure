from fastapi import APIRouter

router = APIRouter(
    prefix='/v1/users'
)

users = ['mano', 'moni', 'aashu']


@router.get('/users')
async def get_users() -> dict:
    """
    Get the list of users
    :return: dict
    """
    return {'users': users}

@router.get('/user/{user}')
async def get_user(user: str) -> dict:
    """
    get specified user
    :return: dict
    """
    return {'users': user}

@router.post('/users')
async def add_user(user: str) -> dict :
    """
    Add user
    :param user: List of user to add
    :return:
    """
    users.append(user)
    return {'users': users}