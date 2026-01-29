pkgname = "python-pikepdf"
pkgver = "10.2.0"
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
sha256 = "749dc71cb3dd2180a77a2a40832d53260fcf39a1b1ece9fe780aff103ea37ac5"
# uses invalid options for pytest in pyproject.toml
options = ["!check"]

