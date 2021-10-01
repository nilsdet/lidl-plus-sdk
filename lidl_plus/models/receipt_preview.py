from dataclasses import dataclass
from typing import Optional

from .currency import Currency


@dataclass
class ReceiptPreview:
    id: str
    isFavorite: bool
    date: str
    totalAmount: str
    storeCode: str
    currency: Currency
    articlesCount: int
    couponsUsedCount: int
    hasReturnedItems: bool
    returnedAmount: str
    invoiceRequestId: Optional[str]
    invoiceId: Optional[str]


@dataclass
class ReceiptPreviewPage:
    page: int
    size: int
    totalCount: int
    records: list[ReceiptPreview]
