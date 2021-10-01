from dataclasses import dataclass
from typing import Optional


@dataclass
class StoreLocation:
    latitude: float
    longitude: float


@dataclass
class StoreCountryZone:
    zoneId: str
    isPilot: bool


@dataclass
class Store:
    storeKey: str
    name: str
    schedule: str
    address: str
    postalCode: str
    locality: str
    isLidlPlus: bool
    location: StoreLocation
    hasParkingForDisabled: bool
    hasParking: bool
    hasBackery: bool
    hasPackage: bool
    province: str
    countryZone: Optional[StoreCountryZone]
