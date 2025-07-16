"""
A utility package that provides `brand.yml` definition for applying
UNDP-branded styling in Shiny and Quarto projects.
"""

from importlib import resources

from brand_yml import Brand

__all__ = ["brand"]

brand = Brand.from_yaml(resources.files().joinpath("_brand.yml"))
