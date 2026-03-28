pkgname = "python-pikepdf"
pkgver = "10.5.0"
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
checkdepends = [
    "python-pytest",
]
pkgdesc = "Python library for reading and writing PDF files"
license = "MPL-2.0"
url = "https://github.com/pikepdf/pikepdf"
source = (
    f"https://github.com/pikepdf/pikepdf/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "57658af585a720daa6cac9baeb6b1677e051e3a6dfc76ca4a5c08e580f7a9edf"
# uses invalid options for pytest in pyproject.toml
options = ["!check"]
