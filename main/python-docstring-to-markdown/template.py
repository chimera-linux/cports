pkgname = "python-docstring-to-markdown"
pkgver = "0.17"
pkgrel = 0
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
sha256 = "df72a112294c7492487c9da2451cae0faeee06e86008245c188c5761c9590ca3"
