"""Select platform for getAir ventilation mode control."""
from __future__ import annotations

import logging

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MODES, MODES_REVERSE

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up getAir select entities."""
    data = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        GetAirModeSelect(
            coordinator=data["coordinator"],
            client=data["client"],
            device_id=data["device_id"],
            entry_id=entry.entry_id,
        )
    ])


class GetAirModeSelect(CoordinatorEntity, SelectEntity):
    """Select the getAir ventilation mode."""

    _attr_name = "Ventilation Mode"
    _attr_options = list(MODES.keys())
    _attr_icon = "mdi:air-filter"

    def __init__(self, coordinator, client, device_id, entry_id):
        super().__init__(coordinator)
        self._client = client
        self._device_id = device_id
        self._attr_unique_id = f"{entry_id}_ventilation_mode_control"
        self._attr_device_info = {
            "identifiers": {(DOMAIN, device_id)},
            "name": "getAir ComfortControl Pro BT",
            "manufacturer": "getAir",
            "model": "ComfortControl Pro BT",
        }

    @property
    def current_option(self) -> str | None:
        if self.coordinator.data is None:
            return None
        api_mode = self.coordinator.data["zone"].get("mode")
        return MODES_REVERSE.get(api_mode, api_mode)

    async def async_select_option(self, option: str) -> None:
        """Set the ventilation mode."""
        api_mode = MODES.get(option)
        if api_mode is None:
            _LOGGER.error("Unknown mode: %s", option)
            return
        _LOGGER.debug("Setting getAir mode to %s (%s)", option, api_mode)
        await self._client.set_zone_property(self._device_id, {"mode": api_mode})
        await self.coordinator.async_request_refresh()
