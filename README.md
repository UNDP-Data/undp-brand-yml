# undp-brand-yml

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License](https://img.shields.io/github/license/undp-data/undp-brand-yml)](https://github.com/undp-data/undp-brand-yml/blob/main/LICENSE)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

A Python package that provides a [`brand.yml`](https://posit-dev.github.io/brand-yml/) definition for applying UNDP-branded styling in Shiny and Quarto projects. The project is based on the corporate guidelines from [UNDP Brand](https://brand.undp.org), [UNDP Design System](https://design.undp.org) and [UNDP data viz library](https://dataviz.design.undp.org).

> [!WARNING]  
> The specifications in the `_brand.yml` provided in this package are currently under development. Prior to `v1.0.0`, this package should be considered experimental. Consult the resources above for detailed guidance on corporate branding. For ideas and feedback, feel free to [open an issue](https://github.com/UNDP-Data/undp-brand-yml/issues).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

Currently, the package is distributed via GitHub only. You can install it with `pip`:

```bash
# latest version
 pip install git+https://github.com/undp-data/undp-brand-yml

# specific release version
 pip install git+https://github.com/undp-data/undp-brand-yml.git@0.1.0
```

You can also add it to your `requirements.txt`:

```requirements
undp-brand-yml @ git+https://github.com/undp-data/undp-brand-yml
```

See [VCS Support](https://pip.pypa.io/en/stable/topics/vcs-support/#vcs-support) for more details.

## Usage

The package is designed to provide "ground truth" definitions for some of the core corporate design aspects, including logos, colours and fonts. It is mainly intended to be used as a dependency in other packages and projects. But you can also use it directly to get definitions of interest:

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
print(brand.defaults["sequential_neutral_5"])
```

As stated in [the documentation](https://quarto.org/docs/authoring/brand.html), Quarto provides built-in support for `_brand.yml`. You can easily add UNDP's `_brand.yml` to your project by running the following command in your terminal:

```sh
python -m undp_brand_yml
```

Alternatively, you can modify your `_quarto.yml` to include a `pre-render` command:

```yml
project:
  title: "Untitled"
  pre-render: python -m undp_brand_yml
```

This will ensure the corporate `_brand.yml` is added to your project every time you render your document. By default, the command will do nothing if `_brand.yml` file already exists in the project, so if you have modified the file, your changes will not be overwritten.

> [!IMPORTANT]  
> `_brand.yml` provides just a starting point for styling projects and by no means replaces the corporate guidelines. Adding the file to your project alone will not suffice to align its design with the guidelines. You will most likely need to complement it with custom CSS or templates to improve the look and feel of your outputs. We plan on providing templates for several Quarto formats in the future.

## Features

The package ships a `brand.yml` file with definitions based on the corporate guidelines. Its main purpose is to be a dependency for other packages and projects, while its features include:

- Metadata, logo, colour and typography definitions in line with the UNDP Design System and UNDP data viz library.
- Additional definitions for colour schemes and icons.
- A single dependency (`brand-yml`).

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