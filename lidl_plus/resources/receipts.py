from typing import Iterator

from dacite import from_dict

from .base import Resource
from ..models import ReceiptPreviewPage


class Receipts(Resource):
    def __call__(self, page: int = 1) -> Iterator[ReceiptPreviewPage]:
        url = (
            "https://appgateway.lidlplus.com/tickets/api/v1"
            f"/{self.client.country}/list/{page}"
        )
        r = self.client.session.get(url)

        page = from_dict(ReceiptPreviewPage, r.json())

        yield page

        if page.page * page.size < page.totalCount:
            yield from self(page=page.page + 1)

    def get(self, id: str):
        # todo
        url = self.client.gateway("v24") + f"/tickets/{id}"
        r = self.client.session.get(url)
