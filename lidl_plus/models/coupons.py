from dataclasses import dataclass
from typing import Optional


@dataclass
class ProductText:
    LanguageCode: str
    MarketingDescription: str
    # Quantity: Optional[float] # todo don't know the type yet


@dataclass
class Product:
    Id: int
    Description: str
    Text: ProductText
    Image: str
    Brand: Optional[str]


@dataclass
class Coupon:
    Id: str
    Image: str
    Type: str
    OfferTitle: str
    Title: str
    OfferDescription: str
    OfferDescriptionShort: str
    Description: str
    # FamilyOfInterest # todo don't know the type
    Characteristics: list[str]
    StartDisplayDate: str
    StartValidityDate: str
    EndValidityDate: str
    Brand: Optional[str]
    FooterTitle: str
    FooterDescription: str
    Url: Optional[str]
    Blocked: bool
    Featured: bool
    IsActivated: bool
    BlockedTitle: Optional[str]
    BlockedDescription: str
    BlockedText: Optional[str]
    ApologizeText: str
    ApologizeStatus: bool
    ApologizeTitle: str
    Block1Description: Optional[str]
    Block1Title: Optional[str]
    Block2Description: str
    Block2Title: str
    TicketInfo: str
    PromotionId: str
    Products: list[Product]
    # ProductsDiscounted: list # todo don't know the type yet
    # Stores: list # todo don't know the type yet
    DaysToExpire: str
    SegmentId: Optional[str]
    TagTitle: Optional[str]
    TagSpecial: str
    FirstColor: str
    SecondaryColor: str
    FirstFontColor: str
    SecondaryFontColor: str
    Category: str
    IsSpecial: bool
    HasAlcoholicArticles: bool
    HasAsterisk: bool
