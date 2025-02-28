import os

from beartype import BeartypeConf, BeartypeStrategy
from beartype.claw import beartype_this_package

# beartype can be turned off by setting DISABLE_BEARTYPE environment variable
_beartype_strategy = (
    BeartypeStrategy.O0
    if os.getenv("DISABLE_BEARTYPE") is not None
    else BeartypeStrategy.O0
)

beartype_this_package(conf=BeartypeConf(strategy=_beartype_strategy))
