from dacite import from_dict

from .base import Resource
from ..models import Store


class Stores(Resource):
    def __call__(self) -> list[Store]:
        url = self.client.gateway("v19") + "/stores"
        r = self.client.session.get(url)
        return [from_dict(Store, store) for store in r.json()]

    def get(self, key: str) -> Store:
        url = self.client.gateway("v15") + f"/stores/{key}"
        r = self.client.session.get(url)
        return from_dict(Store, r.json())
