from .data_bridge import to_plain
from ..internal.wave3 import wave3 as Internalwave3
from ...api import EcoflowApiClient
from ...sensor import StatusSensorEntity


class wave3(Internalwave3):

    def _prepare_data(self, raw_data) -> dict[str, any]:
        res = super()._prepare_data(raw_data)
        res = to_plain(res)
        return res

    def _status_sensor(self, client: EcoflowApiClient) -> StatusSensorEntity:
        return StatusSensorEntity(client, self)

