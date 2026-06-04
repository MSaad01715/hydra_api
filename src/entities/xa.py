from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from core.database import Base

class xa(Base):
    __tablename__ = "xa"
    
    # Primary Key
    EndItemAcronymCode = Column(
        "end_item_acronym_code",
        String,
        primary_key=True,
        index=True
    )

    # Business Fields
    AdministrativeLeadTime = Column(
        "administrative_lead_time",
        Integer,
        nullable=True
    )

    ContractNumber = Column(
        "contract_number",
        String,
        nullable=True
    )

    ContactTeamDelayTime = Column(
        "contact_team_delay_time",
        Integer,
        nullable=True
    )

    CostPerReorderAction = Column(
        "cost_per_reorder_action",
        Float,
        nullable=True
    )

    CostPerRequisition = Column(
        "cost_per_requisition",
        Float,
        nullable=True
    )

    DemilitarizationCost = Column(
        "demilitarization_cost",
        Float,
        nullable=True
    )

    DiscountRate = Column(
        "discount_rate",
        Float,
        nullable=True
    )

    EstimatedSalvageValue = Column(
        "estimated_salvage_value",
        Float,
        nullable=True
    )

    HoldingCostPercentage = Column(
        "holding_cost_percentage",
        Float,
        nullable=True
    )

    InitialBinCost = Column(
        "initial_bin_cost",
        Float,
        nullable=True
    )

    InitialCatalogingCost = Column(
        "initial_cataloging_cost",
        Float,
        nullable=True
    )

    InterestRate = Column(
        "interest_rate",
        Float,
        nullable=True
    )

    InventoryStorageSpaceCost = Column(
        "inventory_storage_space_cost",
        Float,
        nullable=True
    )

    LoadingFactor = Column(
        "loading_factor",
        Float,
        nullable=True
    )

    LogisticSupportAnalysisControlNumberStructure = Column(
        "logistic_support_analysis_control_number_structure",
        String,
        nullable=True
    )

    OperationLevel = Column(
        "operation_level",
        String,
        nullable=True
    )

    OperationLife = Column(
        "operation_life",
        Integer,
        nullable=True
    )

    PersonnelTurnoverRateCivilian = Column(
        "personnel_turnover_rate_civilian",
        Float,
        nullable=True
    )

    PersonnelTurnoverRateMilitary = Column(
        "personnel_turnover_rate_military",
        Float,
        nullable=True
    )

    ProductivityFactor = Column(
        "productivity_factor",
        Float,
        nullable=True
    )

    RecurringBinCost = Column(
        "recurring_bin_cost",
        Float,
        nullable=True
    )

    RecurringCatalogingCost = Column(
        "recurring_cataloging_cost",
        Float,
        nullable=True
    )

    RetailStockageCriteria = Column(
        "retail_stock_criteria",
        String,
        nullable=True
    )

    SafetyLevel = Column(
        "safety_level",
        Float,
        nullable=True
    )

    SupportOfSupportEquipmentCostFactor = Column(
        "support_of_support_equipment_cost_facter",
        Float,
        nullable=True
    )

    TransportationCost = Column(
        "transportation_cost",
        Float,
        nullable=True
    )

    TypeAcquisition = Column(
        "type_acquisition",
        String,
        nullable=True
    )

    TypeOfSupplySystemCode = Column(
        "type_of_supply_system_code",
        String,
        nullable=True
    )

    EndItemCurrencyCode = Column(
        "end_item_currency_code",
        String,
        nullable=True
    )

    # Audit / System Fields
    IsActive = Column(
        "is_active",
        Boolean,
        nullable=True
    )

    SortNumber = Column(
        "sort_number",
        Integer,
        nullable=True
    )

    # IsVerified = Column(
    #     "is_verified",
    #     Boolean,
    #     nullable=True
    # )

    # DeactivatedOn = Column(
    #     "deactivated_on",
    #     DateTime,
    #     nullable=True
    # )

    # DeactivatedBy = Column(
    #     "deactivated_by",
    #     String,
    #     nullable=True
    # )

    CreatedOn = Column(
        "created_on",
        DateTime,
        nullable=True
    )

    CreatedBy = Column(
        "created_by",
        String,
        nullable=True
    )


    ModifiedBy = Column(
        "modified_by",
        String,
        nullable=True
    )

    ModifiedOn = Column(
        "modified_on",
        DateTime,
        nullable=True
    )

    Version = Column(
        "version",
        Integer,
        nullable=True
    )

    IsDeleted = Column(
        "is_deleted",
        Boolean,
        nullable=True
    )

    DeletedOn = Column(
        "deleted_on",
        DateTime,
        nullable=True
    )

    DeletedBy = Column(
        "deleted_by",
        String,
        nullable=True
    )

    HashValue = Column(
        "hash_value",
        String,
        nullable=True
    )


    # AuthorId = Column(
    #     "author_id",
    #     Integer,
    #     nullable=True
    # )