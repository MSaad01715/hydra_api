from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class xa_dto(BaseModel):
    EndItemAcronymCode: str
    AdministrativeLeadTime: Optional[int] = None
    CostPerRequisition: Optional[float] = None
    InventoryStorageSpaceCost: Optional[float] = None
    RecurringBinCost: Optional[float] = None
    TypeAcquisition: Optional[str] = None
    DemilitarizationCost: Optional[float] = None
    LoadingFactor: Optional[float] = None
    RecurringCatalogingCost: Optional[float] = None
    TypeOfSupplySystemCode: Optional[str] = None
    DiscountRate: Optional[float] = None
    LogisticSupportAnalysisControlNumberStructure: Optional[str] = None
    RetailStockageCriteria: Optional[str] = None
    EstimatedSalvageValue: Optional[float] = None
    OperationLevel: Optional[str] = None
    SafetyLevel: Optional[float] = None
    HoldingCostPercentage: Optional[float] = None
    OperationLife: Optional[int] = None
    ContractNumber: Optional[str] = None
    InitialBinCost: Optional[float] = None
    PersonnelTurnoverRateCivilian: Optional[float] = None
    SupportOfSupportEquipmentCostFactor: Optional[float] = None
    ContactTeamDelayTime: Optional[int] = None
    InitialCatalogingCost: Optional[float] = None
    PersonnelTurnoverRateMilitary: Optional[float] = None
    TransportationCost: Optional[float] = None
    CostPerReorderAction: Optional[float] = None
    InterestRate: Optional[float] = None
    ProductivityFactor: Optional[float] = None
    EndItemCurrencyCode: Optional[str] = None
    # IsActive: Optional[bool] = None
    # SortNumber: Optional[int] = None