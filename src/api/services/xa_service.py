from ..repositories import readonly_xa_repository as read_repository
from dtos.xa_dto import xa_dto

async def get_all_end_item_acronym_codes():
    repo = read_repository()
    xa_entities = await repo.get_all_async()
    xa_dtos = []
    for item in xa_entities:
        dto = xa_dto(EndItemAcronymCode=item.EndItemAcronymCode)
        dto.AdministrativeLeadTime = item.AdministrativeLeadTime
        dto.ContractNumber = item.ContractNumber
        dto.CostPerRequisition = item.CostPerRequisition
        dto.CostPerReorderAction = item.CostPerReorderAction
        dto.ContactTeamDelayTime = item.ContactTeamDelayTime
        dto.DiscountRate = item.DiscountRate
        dto.DemilitarizationCost = item.DemilitarizationCost
        dto.EndItemCurrencyCode = item.EndItemCurrencyCode
        dto.EstimatedSalvageValue = item.EstimatedSalvageValue
        dto.HoldingCostPercentage = item.HoldingCostPercentage
        dto.InitialBinCost = item.InitialBinCost
        dto.InitialCatalogingCost = item.InitialCatalogingCost
        dto.InterestRate = item.InterestRate
        dto.InventoryStorageSpaceCost = item.InventoryStorageSpaceCost
        dto.LoadingFactor = item.LoadingFactor
        dto.LogisticSupportAnalysisControlNumberStructure = item.LogisticSupportAnalysisControlNumberStructure
        dto.OperationLevel = item.OperationLevel
        dto.PersonnelTurnoverRateCivilian = item.PersonnelTurnoverRateCivilian
        dto.PersonnelTurnoverRateMilitary = item.PersonnelTurnoverRateMilitary
        dto.ProductivityFactor = item.ProductivityFactor
        dto.OperationLife = item.OperationLife
        dto.RecurringCatalogingCost = item.RecurringCatalogingCost
        dto.RecurringBinCost = item.RecurringBinCost
        dto.RetailStockageCriteria = item.RetailStockageCriteria
        dto.SafetyLevel = item.SafetyLevel
        dto.SupportOfSupportEquipmentCostFactor = item.SupportOfSupportEquipmentCostFactor
        dto.TransportationCost = item.TransportationCost
        dto.TypeAcquisition = item.TypeAcquisition
        dto.TypeOfSupplySystemCode = item.TypeOfSupplySystemCode
        xa_dtos.append(dto)
    return xa_dtos

async def get_end_item_acronym_code_by_id(eiac: str):
    repo = read_repository()
    item = await repo.get_by_id_async(eiac)
    if item.EndItemAcronymCode:
        dto = xa_dto(EndItemAcronymCode=item.EndItemAcronymCode)
        dto.AdministrativeLeadTime = item.AdministrativeLeadTime
        dto.ContractNumber = item.ContractNumber
        dto.CostPerRequisition = item.CostPerRequisition
        dto.CostPerReorderAction = item.CostPerReorderAction
        dto.ContactTeamDelayTime = item.ContactTeamDelayTime
        dto.DiscountRate = item.DiscountRate
        dto.DemilitarizationCost = item.DemilitarizationCost
        dto.EndItemCurrencyCode = item.EndItemCurrencyCode
        dto.EstimatedSalvageValue = item.EstimatedSalvageValue
        dto.HoldingCostPercentage = item.HoldingCostPercentage
        dto.InitialBinCost = item.InitialBinCost
        dto.InitialCatalogingCost = item.InitialCatalogingCost
        dto.InterestRate = item.InterestRate
        dto.InventoryStorageSpaceCost = item.InventoryStorageSpaceCost
        dto.LoadingFactor = item.LoadingFactor
        dto.LogisticSupportAnalysisControlNumberStructure = item.LogisticSupportAnalysisControlNumberStructure
        dto.OperationLevel = item.OperationLevel
        dto.PersonnelTurnoverRateCivilian = item.PersonnelTurnoverRateCivilian
        dto.PersonnelTurnoverRateMilitary = item.PersonnelTurnoverRateMilitary
        dto.ProductivityFactor = item.ProductivityFactor
        dto.OperationLife = item.OperationLife
        dto.RecurringCatalogingCost = item.RecurringCatalogingCost
        dto.RecurringBinCost = item.RecurringBinCost
        dto.RetailStockageCriteria = item.RetailStockageCriteria
        dto.SafetyLevel = item.SafetyLevel
        dto.SupportOfSupportEquipmentCostFactor = item.SupportOfSupportEquipmentCostFactor
        dto.TransportationCost = item.TransportationCost
        dto.TypeAcquisition = item.TypeAcquisition
        dto.TypeOfSupplySystemCode = item.TypeOfSupplySystemCode
    return dto

async def create_or_update_end_item_acronym_code(eiac: str, end_item_acronym_code:xa_dto):
    pass

async def patch_end_item_acronym_code(eiac: str, key: str, value: str):
    pass

async def remove_end_item_acronym_code(eiac:str):
    pass