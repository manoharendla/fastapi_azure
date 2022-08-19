from fastapi import APIRouter

router = APIRouter(
    prefix='/v1/admins'
)

admins = ['admin1', 'admin2', 'aashu']


@router.get('/admins')
async def get_admins() -> dict:
    """
    Get the list of admins
    :return: dict
    """
    return {'admins': admins}

@router.get('/admin/{admin}')
async def get_admin(admin: str) -> dict:
    """
    get specified admin
    :return: dict
    """
    return {'admins': admin}

@router.post('/admins')
async def add_admin(admin: str) -> dict :
    """
    Add admin
    :param admin: List of admin to add
    :return:
    """
    admins.append(admin)
    return {'admins': admins}