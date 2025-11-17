"""
Plotting extras to apply UNDP-branding to supported data visualisation libraries.
"""

from typing import Literal

try:
    import plotly.io as pio
except ImportError:
    raise RuntimeError(
        "To use plotting modules, `plotting` extras is required. To install it, run "
        "`pip install undp-brand-yml[plotting] @ git+https://github.com/undp-data/undp-brand-yml`"
    )

from . import plotly_themes

__all__ = ["set_plotly_theme"]


def set_plotly_theme(name: Literal["light", "dark"] = "light") -> None:
    """
    Set a UNDP-branded theme for Plotly figures.

    Parameters
    ----------
    name : {'light', 'dark'}, default='light'
        Name of the theme to apply.

    Returns
    -------
    None
        The theme is set as the default. No value is returned.
    """
    match name:
        case "light":
            theme = plotly_themes.LIGHT
        case "dark":
            theme = plotly_themes.DARK
        case _:
            raise ValueError(f"{name:!r} name is not supported.")
    pio.templates["undp"] = theme
    pio.templates.default = "undp"
