"""Common Jinja2 filters for manipulating ansible vars."""

import math


def ceil2(number: int, min_value=0) -> int:
    """Round up number to the next highest power of 2."""
    ceiled = 2 ** int(math.ceil(math.log(number, 2))) if number > 0 else 0
    return max(ceiled, min_value)


class FilterModule:
    """Common Jinja2 filters for manipulating ansible vars."""

    def filters(self):
        """Return filter functions."""
        return {
            "ceil2": ceil2,
        }
