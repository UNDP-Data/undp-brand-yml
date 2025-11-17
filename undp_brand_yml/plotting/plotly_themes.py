"""
Custom theme templates for Plotly based on UNDP data viz library.
"""

import plotly.graph_objects as go

from ..brand import brand

__all__ = ["LIGHT", "DARK"]

LIGHT = go.layout.Template(
    layout={
        "annotationdefaults": {
            "arrowcolor": brand.color.palette["gray-700"],
            "arrowhead": 0,
            "arrowwidth": 1,
        },
        "autotypenumbers": "strict",
        "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
        "colorscale": {
            "diverging": brand.defaults["diverging"],
            "sequential": brand.defaults["sequential_neutral"],
            "sequentialminus": brand.defaults["sequential_neutral"][::-1],
        },
        "colorway": brand.defaults["categorical"],
        "font": {
            "color": brand.color.palette["gray-700"],
            "family": f"{brand.typography.base.family}, sans-serif",
        },
        "geo": {
            "bgcolor": "white",
            "lakecolor": "white",
            "landcolor": "white",
            "showlakes": True,
            "showland": True,
            "subunitcolor": brand.color.palette["gray-400"],
        },
        "hoverlabel": {"align": "left"},
        "hovermode": "closest",
        "mapbox": {"style": "light"},
        "paper_bgcolor": "white",
        "plot_bgcolor": "white",
        "polar": {
            "angularaxis": {
                "gridcolor": brand.color.palette["gray-300"],
                "linecolor": brand.color.palette["gray-300"],
                "ticks": "",
            },
            "bgcolor": "white",
            "radialaxis": {
                "gridcolor": brand.color.palette["gray-300"],
                "linecolor": brand.color.palette["gray-300"],
                "ticks": "",
            },
        },
        "scene": {
            "xaxis": {
                "backgroundcolor": "white",
                "gridcolor": brand.color.palette["gray-400"],
                "gridwidth": 2,
                "linecolor": brand.color.palette["gray-300"],
                "showbackground": True,
                "ticks": "",
                "zerolinecolor": brand.color.palette["gray-300"],
            },
            "yaxis": {
                "backgroundcolor": "white",
                "gridcolor": brand.color.palette["gray-400"],
                "gridwidth": 2,
                "linecolor": brand.color.palette["gray-300"],
                "showbackground": True,
                "ticks": "",
                "zerolinecolor": brand.color.palette["gray-300"],
            },
            "zaxis": {
                "backgroundcolor": "white",
                "gridcolor": brand.color.palette["gray-400"],
                "gridwidth": 2,
                "linecolor": brand.color.palette["gray-300"],
                "showbackground": True,
                "ticks": "",
                "zerolinecolor": brand.color.palette["gray-300"],
            },
        },
        "shapedefaults": {"line": {"color": brand.color.palette["gray-700"]}},
        "ternary": {
            "aaxis": {
                "gridcolor": brand.color.palette["gray-400"],
                "linecolor": brand.color.palette["gray-500"],
                "ticks": "",
            },
            "baxis": {
                "gridcolor": brand.color.palette["gray-400"],
                "linecolor": brand.color.palette["gray-500"],
                "ticks": "",
            },
            "bgcolor": "white",
            "caxis": {
                "gridcolor": brand.color.palette["gray-400"],
                "linecolor": brand.color.palette["gray-500"],
                "ticks": "",
            },
        },
        "title": {"x": 0.05},
        "xaxis": {
            "automargin": True,
            "gridcolor": brand.color.palette["gray-300"],
            "griddash": "dash",
            "linecolor": brand.color.palette["gray-300"],
            "ticks": "",
            "title": {"standoff": 15},
            "zerolinecolor": brand.color.palette["gray-300"],
            "zerolinewidth": 2,
        },
        "yaxis": {
            "automargin": True,
            "gridcolor": brand.color.palette["gray-300"],
            "griddash": "dash",
            "linecolor": brand.color.palette["gray-300"],
            "ticks": "",
            "title": {"standoff": 15},
            "zerolinecolor": brand.color.palette["gray-300"],
            "zerolinewidth": 2,
        },
    }
)

DARK = go.layout.Template(
    layout={
        "annotationdefaults": {
            "arrowcolor": brand.color.palette["gray-200"],
            "arrowhead": 0,
            "arrowwidth": 1,
        },
        "autotypenumbers": "strict",
        "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
        "colorscale": {
            "diverging": brand.defaults["diverging"][::-1],
            "sequential": brand.defaults["sequential_neutral"][::-1],
            "sequentialminus": brand.defaults["sequential_neutral"],
        },
        "colorway": brand.defaults["categorical"],
        "font": {
            "color": brand.color.palette["gray-200"],
            "family": f"{brand.typography.base.family}, sans-serif",
        },
        "geo": {
            "bgcolor": brand.color.palette["gray-700"],
            "lakecolor": brand.color.palette["gray-700"],
            "landcolor": brand.color.palette["gray-700"],
            "showlakes": True,
            "showland": True,
            "subunitcolor": brand.color.palette["gray-300"],
        },
        "hoverlabel": {"align": "left"},
        "hovermode": "closest",
        "mapbox": {"style": "light"},
        "paper_bgcolor": brand.color.palette["gray-700"],
        "plot_bgcolor": brand.color.palette["gray-700"],
        "polar": {
            "angularaxis": {
                "gridcolor": brand.color.palette["gray-500"],
                "linecolor": brand.color.palette["gray-500"],
                "ticks": "",
            },
            "bgcolor": brand.color.palette["gray-700"],
            "radialaxis": {
                "gridcolor": brand.color.palette["gray-500"],
                "linecolor": brand.color.palette["gray-500"],
                "ticks": "",
            },
        },
        "scene": {
            "xaxis": {
                "backgroundcolor": brand.color.palette["gray-700"],
                "gridcolor": brand.color.palette["gray-300"],
                "gridwidth": 2,
                "linecolor": brand.color.palette["gray-500"],
                "showbackground": True,
                "ticks": "",
                "zerolinecolor": brand.color.palette["gray-500"],
            },
            "yaxis": {
                "backgroundcolor": brand.color.palette["gray-700"],
                "gridcolor": brand.color.palette["gray-300"],
                "gridwidth": 2,
                "linecolor": brand.color.palette["gray-500"],
                "showbackground": True,
                "ticks": "",
                "zerolinecolor": brand.color.palette["gray-500"],
            },
            "zaxis": {
                "backgroundcolor": brand.color.palette["gray-700"],
                "gridcolor": brand.color.palette["gray-300"],
                "gridwidth": 2,
                "linecolor": brand.color.palette["gray-500"],
                "showbackground": True,
                "ticks": "",
                "zerolinecolor": brand.color.palette["gray-500"],
            },
        },
        "shapedefaults": {"line": {"color": brand.color.palette["gray-200"]}},
        "ternary": {
            "aaxis": {
                "gridcolor": brand.color.palette["gray-300"],
                "linecolor": brand.color.palette["gray-200"],
                "ticks": "",
            },
            "baxis": {
                "gridcolor": brand.color.palette["gray-300"],
                "linecolor": brand.color.palette["gray-200"],
                "ticks": "",
            },
            "bgcolor": brand.color.palette["gray-700"],
            "caxis": {
                "gridcolor": brand.color.palette["gray-300"],
                "linecolor": brand.color.palette["gray-200"],
                "ticks": "",
            },
        },
        "title": {"x": 0.05},
        "xaxis": {
            "automargin": True,
            "gridcolor": brand.color.palette["gray-500"],
            "griddash": "dash",
            "linecolor": brand.color.palette["gray-500"],
            "ticks": "",
            "title": {"standoff": 15},
            "zerolinecolor": brand.color.palette["gray-500"],
            "zerolinewidth": 2,
        },
        "yaxis": {
            "automargin": True,
            "gridcolor": brand.color.palette["gray-500"],
            "griddash": "dash",
            "linecolor": brand.color.palette["gray-500"],
            "ticks": "",
            "title": {"standoff": 15},
            "zerolinecolor": brand.color.palette["gray-500"],
            "zerolinewidth": 2,
        },
    }
)
