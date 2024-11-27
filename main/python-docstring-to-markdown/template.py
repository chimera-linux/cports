pkgname = "python-docstring-to-markdown"
pkgver = "0.15"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python module for converting docstrings to markdown"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/python-lsp/docstring-to-markdown"
source = f"$(PYPI_SITE)/d/docstring-to-markdown/docstring-to-markdown-{pkgver}.tar.gz"
sha256 = "e146114d9c50c181b1d25505054a8d0f7a476837f0da2c19f07e06eaed52b73d"
