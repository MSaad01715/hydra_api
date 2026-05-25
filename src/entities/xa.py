from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from core.database import Base

class xa(Base):
    __tablename__ = "GEIA_XA"
    
    # Primary Key
    EndItemAcronymCode = Column(
        String,
        primary_key=True,
        index=True
    )

    # Business Fields
    AdministrativeLeadTime = Column(
        Integer,
        nullable=True
    )

    ContractNumber = Column(
        String,
        nullable=True
    )

    ContactTeamDelayTime = Column(
        Integer,
        nullable=True
    )

    CostPerReorderAction = Column(
        Float,
        nullable=True
    )

    CostPerRequisition = Column(
        Float,
        nullable=True
    )

    DemilitarizationCost = Column(
        Float,
        nullable=True
    )

    DiscountRate = Column(
        Float,
        nullable=True
    )

    EstimatedSalvageValue = Column(
        Float,
        nullable=True
    )

    HoldingCostPercentage = Column(
        Float,
        nullable=True
    )

    InitialBinCost = Column(
        Float,
        nullable=True
    )

    InitialCatalogingCost = Column(
        Float,
        nullable=True
    )

    InterestRate = Column(
        Float,
        nullable=True
    )

    InventoryStorageSpaceCost = Column(
        Float,
        nullable=True
    )

    LoadingFactor = Column(
        Float,
        nullable=True
    )

    LogisticSupportAnalysisControlNumberStructure = Column(
        String,
        nullable=True
    )

    OperationLevel = Column(
        String,
        nullable=True
    )

    OperationLife = Column(
        Integer,
        nullable=True
    )

    PersonnelTurnoverRateCivilian = Column(
        Float,
        nullable=True
    )

    PersonnelTurnoverRateMilitary = Column(
        Float,
        nullable=True
    )

    ProductivityFactor = Column(
        Float,
        nullable=True
    )

    RecurringBinCost = Column(
        Float,
        nullable=True
    )

    RecurringCatalogingCost = Column(
        Float,
        nullable=True
    )

    RetailStockageCriteria = Column(
        String,
        nullable=True
    )

    SafetyLevel = Column(
        Float,
        nullable=True
    )

    SupportOfSupportEquipmentCostFactor = Column(
        Float,
        nullable=True
    )

    TransportationCost = Column(
        Float,
        nullable=True
    )

    TypeAcquisition = Column(
        String,
        nullable=True
    )

    TypeOfSupplySystemCode = Column(
        String,
        nullable=True
    )

    EndItemCurrencyCode = Column(
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

    IsVerified = Column(
        "is_verified",
        Boolean,
        nullable=True
    )

    DeactivatedOn = Column(
        "deactivated_on",
        DateTime,
        nullable=True
    )

    DeactivatedBy = Column(
        "deactivated_by",
        String,
        nullable=True
    )

    CreatedBy = Column(
        "created_by",
        String,
        nullable=True
    )

    CreatedOn = Column(
        "created_on",
        DateTime,
        nullable=True
    )

    UpdatedBy = Column(
        "updated_by",
        String,
        nullable=True
    )

    UpdatedOn = Column(
        "updated_on",
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

    DeletedBy = Column(
        "deleted_by",
        String,
        nullable=True
    )

    DeletedOn = Column(
        "deleted_on",
        DateTime,
        nullable=True
    )

    Hash = Column(
        "hash",
        String,
        nullable=True
    )


    AuthorId = Column(
        "author_id",
        Integer,
        nullable=True
    )