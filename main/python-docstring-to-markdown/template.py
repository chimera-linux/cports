pkgname = "python-docstring-to-markdown"
pkgver = "0.16"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python",
    "python-typing_extensions",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python module for converting docstrings to markdown"
license = "LGPL-2.1-or-later"
url = "https://github.com/python-lsp/docstring-to-markdown"
source = f"$(PYPI_SITE)/d/docstring-to-markdown/docstring_to_markdown-{pkgver}.tar.gz"
sha256 = "097bf502fdf040b0d019688a7cc1abb89b98196801448721740e8aa3e5075627"
