# https://github.com/bluewalk/lidlplus-php-client/blob/master/src/LidlPlus/LidlPlus.php
# https://documenter.getpostman.com/view/624585/SW7W6qFq#05f56bdc-6b43-4f7b-b074-962be484663a
import requests

from .resources import Receipts, Stores, Coupons


class LidlPlus:
    def __init__(self, access_token: str, country: str = "DE"):
        self.access_token = access_token
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "User-Agent": "LidlSocialInternacional/14.41.2 (com.lidl.eci.lidl.plus; build:611; iOS 14.7.1) Alamofire/4.8.2",  # noqa: E501
                "Authorization": f"Bearer {self.access_token}",
                "App": "com.lidl.eci.lidl.plus",
                "Operating-System": "iOS",
                "App-Version": "999.99.9",
            }
        )
        self.country = country
        self.coupons = Coupons(self)
        self.receipts = Receipts(self)
        self.stores = Stores(self)

    def gateway(self, version: str) -> str:
        return f"https://appgateway.lidlplus.com/app/{version}/{self.country}"

    def content(self, version: str) -> str:
        return f"https://content.lidlplus.com/{version}/{self.country}"
