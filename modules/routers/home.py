from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def home():
    return { 'message': 'Welcome to the sample fastapi azure app'}
