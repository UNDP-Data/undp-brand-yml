"""
Basic tests for structure and content validation.
"""

import re

import pytest

from undp_brand_yml import brand


@pytest.mark.parametrize("name", ["meta", "color", "logo", "typography", "defaults"])
def test_brand_structure(name: str):
    """
    Test top-level brand structure.
    """
    assert hasattr(brand, name)


def test_meta_structure():
    """
    Test properties in the `meta` section.
    """
    section = brand.meta
    assert hasattr(section, "name")
    assert hasattr(section.name, "full")
    assert hasattr(section.name, "short")
    assert hasattr(section, "link")
    assert hasattr(section.link, "home")
    assert hasattr(section.link, "github")
    assert hasattr(section, "description")


def test_meta_content():
    """
    Test property values in the `meta` section.
    """
    section = brand.meta
    assert section.name.full == "United Nations Development Programme"
    assert section.name.short == "UNDP"
    assert str(section.link.home).startswith("https://www.undp.org")
    assert "the leading United Nations organization" in section.description


def test_logo_structure():
    """
    Test properties in the `logo` section.
    """
    section = brand.logo
    assert hasattr(section, "images")
    assert isinstance(section.images, dict)
    for name in ("small", "medium", "large"):
        assert hasattr(section, name)
        assert hasattr(getattr(section, name), "light")
        assert hasattr(getattr(section, name), "dark")


def test_logo_content():
    """
    Test property values in the `logo` section.
    """
    extensions = (".ico", ".svg", ".webp", ".png")
    for name, resource in brand.logo.images.items():
        assert str(resource.path.root).endswith(
            extensions
        ), f"Unexpected extension for {name}"


def test_color_structure():
    """
    Test properties in the `color` section.
    """
    section = brand.color
    assert hasattr(section, "palette")
    assert isinstance(section.palette, dict)
    assert len(section.palette) > 10, "At least 10 colours are expected"


def test_color_content():
    """
    Test property values in the `color` section.
    """
    for name, value in brand.color.palette.items():
        assert value.startswith("#"), f"Missing hash for {name} colour"
        assert len(value) == 7, f"Incomplete hash value for {name} colour"


def test_typography_structure():
    """
    Test properties in the `typography` section.
    """
    section = brand.typography
    assert hasattr(section, "fonts")
    assert isinstance(section.fonts, list)
    assert hasattr(section, "base")
    assert hasattr(section, "headings")
    assert hasattr(section, "monospace")
    assert hasattr(section, "monospace_inline")
    assert hasattr(section, "monospace_block")
    assert hasattr(section, "link")


def test_typography_content():
    """
    Test property values in the `typography` section.
    """
    section = brand.typography
    assert section.fonts[0].family == "Proxima Nova"
    assert section.base.family == "Proxima Nova"
    assert section.headings.family == "Proxima Nova"


def test_defaults_structure():
    """
    Test properties in the `defaults` section.

    Unlike for other sections, `brand.yml` standard imposes
    little-to-no structure for this one, allowing to store
    virtually arbitrary values.
    """
    section = brand.defaults
    assert section.get("categorical")
    assert section.get("sequential_negative")
    assert section.get("sequential_positive")
    assert section.get("sequential_neutral")
    assert section.get("diverging")


def test_defaults_content():
    """
    Test property values in the `defaults` section.

    Validation assumes that colour schemes have been appropriately
    defined and any numbers at the end indicate the number of colours
    in the scheme.
    """
    for name in brand.defaults:
        if re.match("categorical|sequential|diverging", name):
            assert isinstance(brand.defaults[name], list)
            n = 11 if name == "diverging" else 10
            assert len(brand.defaults[name]) == n
