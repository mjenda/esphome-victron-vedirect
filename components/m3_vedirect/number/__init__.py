from esphome.components import number
import esphome.config_validation as cv
import esphome.const as ec

from .. import VEDirectPlatform, ve_reg


# Home Assistant persists ESPHome entity metadata to JSON.
# NaN values can round-trip as null and break cache reload after restart.
DEFAULT_MIN_VALUE = -1_000_000.0
DEFAULT_MAX_VALUE = 1_000_000.0
DEFAULT_STEP = 1.0


async def _register_number(var, config):
    await number.register_number(
        var,
        config,
        min_value=float(config.get(ec.CONF_MIN_VALUE, DEFAULT_MIN_VALUE)),
        max_value=float(config.get(ec.CONF_MAX_VALUE, DEFAULT_MAX_VALUE)),
        step=float(config.get(ec.CONF_STEP, DEFAULT_STEP)),
    )


PLATFORM = VEDirectPlatform(
    "number",
    number,
    {},
    (ve_reg.CLASS.NUMERIC,),
    False,
    {
        cv.Optional(ec.CONF_MIN_VALUE): cv.float_,
        cv.Optional(ec.CONF_MAX_VALUE): cv.float_,
        cv.Optional(ec.CONF_STEP): cv.positive_float,
    },
    register_entity=_register_number,
)

CONFIG_SCHEMA = PLATFORM.CONFIG_SCHEMA


async def to_code(config: dict):
    await PLATFORM.to_code(config)
