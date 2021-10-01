from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import LidlPlus


class Resource:
    def __init__(self, client: "LidlPlus"):
        self.client = client
