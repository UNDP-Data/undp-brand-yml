"""
Building extension module to include the brand file in the distribution.
See https://python-poetry.org/docs/building-extension-modules.
"""

from urllib.request import urlretrieve


def build() -> None:
    """
    Download the brand YAML file from the extension-for-quarto project.
    """
    urlretrieve(
        "https://raw.githubusercontent.com/UNDP-Data/extensions-for-quarto/refs/heads/main/_extensions/brand-yml/brand.yml",
        "undp_brand_yml/_brand.yml",
    )


if __name__ == "__main__":
    build()
