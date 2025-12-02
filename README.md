# undp-brand-yml

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](https://img.shields.io/github/license/undp-data/undp-brand-yml)](https://github.com/undp-data/undp-brand-yml/blob/main/LICENSE)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![Quarto Publish](https://github.com/UNDP-Data/undp-brand-yml/actions/workflows/publish.yml/badge.svg)](https://github.com/UNDP-Data/undp-brand-yml/actions/workflows/publish.yml)

A Python package that provides the [`brand.yml`](https://posit-dev.github.io/brand-yml/) definition for applying UNDP-branded styling in Shiny and Quarto projects. The project is based on the corporate guidelines from [UNDP Brand](https://brand.undp.org), [UNDP Design System](https://design.undp.org) and [UNDP data viz library](https://dataviz.design.undp.org).

> [!NOTE]  
> This package uses `_brand.yml` file from the brand extension in [`extensions-for-quarto`](https://github.com/UNDP-Data/extensions-for-quarto) project. As of the time of writing, that extension is still under development. Before the release of version `1.0.0` of the extension, this package should be considered experimental. Consult the resources above for the detailed guidance on corporate branding. For ideas and feedback, feel free to [open an issue](https://github.com/UNDP-Data/undp-brand-yml/issues).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

This package is distributed via GitHub only. You can install it with `pip`:

```bash
# latest (unstable) version
pip install git+https://github.com/undp-data/undp-brand-yml

# specific release version
pip install git+https://github.com/undp-data/undp-brand-yml.git@0.2.0

# specific release version with extras
pip install undp-brand-yml[plotting] @ git+https://github.com/undp-data/undp-brand-yml.git@0.2.0
```

Similarly, you can add it to your `requirements.txt`:

```txt
# specific release version (recommended)
undp-brand-yml @ git+https://github.com/undp-data/undp-brand-yml.git@0.2.0
```

See [VCS Support](https://pip.pypa.io/en/stable/topics/vcs-support/#vcs-support) in `pip` documenation for more details.

> [!TIP]
> It is strongly recommended to install the package in a virtual environment. Refer to [Creating virtual environments](https://docs.python.org/3/library/venv.html) section in the Python documentation to learn more about `venv`.

## Usage

The package is designed to provide "ground truth" definitions for some of the core corporate design aspects, including logos, colours, and fonts. It is mainly intended to be used as a dependency in other packages and projects. But you can also use it directly to get definitions of interest.

### Usage in Quarto

Quarto provides built-in multiformat support for `_brand.yml`. To have the branding applied, the brand file must be present in the project directory. You can easily add it to your project by running the following command in your terminal:

```sh
python -m undp_brand_yml
```

Alternatively, you can modify your `_quarto.yml` to include a `pre-render` command:

```yaml
project:
  title: "Project Title"
  pre-render: python -m undp_brand_yml
```

This will ensure the corporate `_brand.yml` is added to your project every time you render your document(s). By default, the command will do nothing if `_brand.yml` file already exists in the project. So, if you have modified the file, your changes will not be overwritten.

> [!IMPORTANT]
> Quarto `1.8.20` introduced support for [brand extensions](https://quarto.org/docs/extensions/brand.html), which are now the recommended way to distribute `_brand.yml` and related files. You should consider using the brand extension instead of using this Python package. Refer to [extensions-for-quarto](https://github.com/UNDP-Data/extensions-for-quarto) project to learn more.

### Usage in Shiny for Python

Like in Quarto projects, Shiny for Python applications require a `_brand.yml` file to be present in your project's directory. However, unlike Quarto, Shiny for Python has no support for brand extensions. You must therefore manually add the file by running the following command in your terminal:

```sh
python -m undp_brand_yml
```

You will also need to modify your `app.py` file to enable branding:

```py
from shiny import ui

app_ui = ui.page_fluid(
    # App UI code...
    theme=ui.Theme.from_brand(__file__)
)
```

> [!TIP]
> Refer to [Branded theming for Shiny for Python apps](https://shiny.posit.co/blog/posts/shiny-python-1.2-brand-yml/) to learn more about `_brand.yml` support in Shiny for Python.

### Usage as a package

For more advanced use cases, you may want to programmatically access the specifications from `_brand.yml`. Here is an example of how you can do so:

```python
from undp_brand_yml import brand

# get the official full name and recommended description
print(brand.meta.name.full)
print(brand.meta.description)

# get official links to webpages and social media accounts
print(brand.meta.link.home)
print(brand.meta.link.linkedin)

# get hex colour values from the official palette, e.g. UNDP Blue
print(brand.color.palette["blue-600"])

# list all the colour names
print(list(brand.color.palette))

# get colour scheme definitions for plotting
print(brand.defaults["categorical"])
print(brand.defaults["sequential_neutral"])
```

### `plotting` extra

> [!IMPORTANT]  
> You must have `plotting` extra installed to make use of the functionality descrived in this section. Refer to [Installation](#installation) section above for details.

If your project includes a data visualisation component, consider using the [`plotly`](https://plotly.com/python) library, whose figures can be easily styled using this package:

```python
import plotly.express as px
from undp_brand_yml.plotting import set_plotly_theme

# set the default theme to UNDP branding
set_plotly_theme()

df = px.data.iris()
fig = px.scatter(data_frame=df, x="petal_length", y="petal_width", color="species")
fig.update_layout(xaxis={"rangemode": "tozero"}, yaxis={"rangemode": "tozero"})
fig.show()
```

> [!TIP]
> For JavaScript projects, consider using [UNDP data viz library](https://github.com/undp/data-visualization).


## Features

The package ships the `_brand.yml` file based on the corporate guidelines. Its main purpose is to be a dependency for other packages and projects. Its features include:

- **Comprehensiveness**: the package provides metadata, logo, colour and typography definitions, all in just one file.
- **Consistency**: the specifications are in line with the UNDP Design System and UNDP data viz library.
- **Versatility**: the package can be used in Quarto or Shiny for Python applications alike. It can also style `plotly` figures using `plotting` extras.
- **Minimalism**: a single required dependency (`brand-yml`).

> [!IMPORTANT]  
> `_brand.yml` provides just a starting point for styling projects and by no means replaces the corporate guidelines. Adding the file to your project alone will often not suffice to fully align its design with the guidelines. You might need to complement it with custom CSS or templates to improve the look and feel of your outputs.

## Contributing

All contributions must follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). The codebase is formatted with `black` and `isort`. Use the provided [Makefile](./Makefile) for these routine operations.

1. Clone or fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Ensure your code is properly formatted (`make format`)
5. Commit your changes (`git commit -m 'Add some feature'`)
6. Push to the branch (`git push origin feature-branch`)
7. Open a pull request

## License

This project is licensed under the BSD 3-Clause License. However, entities or individuals not affiliated with UNDP are strictly prohibited from using this package or any of its components to create, share, publish, or distribute works that resemble, claim affiliation with, or imply endorsement by UNDP.

UNDP’s name, emblem and its abbreviation are the exclusive property of UNDP and are protected under international law. Their unauthorized use is prohibited, and they may not be reproduced or used in any manner without UNDP’s prior written permission.

## Contact

This project is part of [Data Futures Exchange (DFx)](https://data.undp.org) at UNDP. If you are facing any issues or would like to make some suggestions, feel free to [open an issue](https://github.com/undp-data/undp-brand-yml/issues/new/choose). For enquiries about DFx, visit [Contact Us](https://data.undp.org/contact-us).
