from fastapi import APIRouter
from ..services.xa_service import get_all_end_item_acronym_codes

router = APIRouter(
    prefix='/api/v1/xa',
    tags=['end_item_acronym_codes'])

@router.get('/')
async def get_all():
    return await get_all_end_item_acronym_codes()

@router.get('/eiac/{eiac}')
async def get_by_id(eiac:str):
    return eiac

@router.get('/eiac/{eiac}')
async def create_or_update(eiac:str):
    return eiac

@router.get('/eiac/{eiac}')
async def remove(eiac:str):
    return eiac


