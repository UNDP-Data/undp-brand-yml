"""
A brand loader module.
"""

from importlib import resources

from brand_yml import Brand

__all__ = ["brand"]

brand = Brand.from_yaml(resources.files().joinpath("_brand.yml"))
