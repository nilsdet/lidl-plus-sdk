from dacite import from_dict

from .base import Resource
from ..models import Coupon


class Coupons(Resource):
    def __call__(self) -> list[Coupon]:
        url = self.client.content("v1") + "/coupons"
        r = self.client.session.get(
            url, headers={"Authorization": None}
        )  # todo I don't currently know why it does not work with the "Authorization"
        #       header set.
        return [from_dict(Coupon, coupon) for coupon in r.json()]
