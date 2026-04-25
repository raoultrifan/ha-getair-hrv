"""Number platform for getAir fan speed control."""
from __future__ import annotations

import logging

from homeassistant.components.number import NumberEntity, NumberMode
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up getAir number entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        GetAirFanSpeed(
            coordinator=data["coordinator"],
            client=data["client"],
            device_id=data["device_id"],
            entry_id=entry.entry_id,
        )
    ])


class GetAirFanSpeed(CoordinatorEntity, NumberEntity):
    """Control the getAir fan speed."""

    _attr_name = "Fan Speed"
    _attr_native_min_value = 0.0
    _attr_native_max_value = 4.0
    _attr_native_step = 0.5
    _attr_mode = NumberMode.SLIDER
    _attr_icon = "mdi:fan"

    def __init__(self, coordinator, client, device_id, entry_id):
        super().__init__(coordinator)
        self._client = client
        self._device_id = device_id
        self._attr_unique_id = f"{entry_id}_fan_speed_control"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, device_id)},
            "name": "getAir ComfortControl Pro BT",
            "manufacturer": "getAir",
            "model": "ComfortControl Pro BT",
        }

    @property
    def native_value(self) -> float | None:
        if self.coordinator.data is None:
            return None
        return self.coordinator.data["zone"].get("speed")

    async def async_set_native_value(self, value: float) -> None:
        """Set the fan speed."""
        speed = round(value, 1)
        _LOGGER.debug("Setting getAir fan speed to %s", speed)
        await self._client.set_zone_property(self._device_id, {"speed": speed})
        await self.coordinator.async_request_refresh()
