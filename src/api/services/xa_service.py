from ..repositories import ReadOnly_EndItemAcronymCode_Repository as _repository

async def get_all_end_item_acronym_codes():
    return await _repository.get_all_async()