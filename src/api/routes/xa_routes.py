from fastapi import APIRouter, Depends
from ..services.xa_service import (get_all_end_item_acronym_codes, 
                                   get_end_item_acronym_code_by_id, 
                                   create_or_update_end_item_acronym_code,
                                   patch_end_item_acronym_code,
                                   remove_end_item_acronym_code)
from dtos.xa_dto import xa_dto
from dtos.envelop import Envelop

router = APIRouter(
    prefix='/api/v1/xa',
    tags=['end_item_acronym_codes'])

@router.get('/')
async def get_all():
    envelop = Envelop()
    message = ''
    items = []
    # try:
    items = await get_all_end_item_acronym_codes()
    message = 'Processed Ok'
    # except:
    #     print('something went wrong!')
    #     message = 'something went wrong!'

    envelop.TotalRecords = len(items)
    envelop.IsSuccessful = True
    envelop.Content = items
    envelop.Status = message
    return envelop

@router.get('/{eiac}')
async def get_by_id(eiac:str):
    envelop = Envelop()

    message = ''
    items = []
    try:
        items = await get_end_item_acronym_code_by_id(eiac)
        message = 'Processed Ok'
    except:
        print('something went wrong!')
        message = 'something went wrong!'

    envelop.TotalRecords = 1
    envelop.IsSuccessful = True
    envelop.Content = items
    envelop.Status = message

    return envelop

@router.post('/{eiac}')
async def create_or_update(eiac: str, end_item_acronym_code:xa_dto):
    envelop = Envelop()

    message = ''
    items = []
    try:
        items = await create_or_update_end_item_acronym_code(eiac, end_item_acronym_code)
        message = 'Processed Ok'
    except:
        print('something went wrong!')
        message = 'something went wrong!'

    envelop.TotalRecords = 1
    envelop.IsSuccessful = True
    envelop.Content = items
    envelop.Status = message

    return envelop

@router.get('/eiac/{eiac}')
async def remove(eiac:str):
    return eiac


