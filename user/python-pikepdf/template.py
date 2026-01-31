pkgname = "python-pikepdf"
pkgver = "10.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-pybind11",
    "python-setuptools",
]
makedepends = [
    "python-devel",
    "qpdf-devel",
]
# checkdepends = [
#     "python-pytest",
# ]
pkgdesc = "Lossless conversion of raster images to PDF"
license = "MPL-2.0"
url = "https://github.com/pikepdf/pikepdf"
source = f"https://github.com/pikepdf/pikepdf/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bc792cf00acc39ea38243b6279b4cd9014909e6e8567d33c7ec84fe259dad4cc"
# uses invalid options for pytest in pyproject.toml
options = ["!check"]

