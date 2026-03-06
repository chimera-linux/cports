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
checkdepends = [
    "python-pytest",
]
pkgdesc = "Python library for reading and writing PDF files"
license = "MPL-2.0"
url = "https://github.com/pikepdf/pikepdf"
source = (
    f"https://github.com/pikepdf/pikepdf/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "235e0ad77545a9e8b5bdc63a9f30500e50fc502c92372c0d056a1134c7b65ea6"
# uses invalid options for pytest in pyproject.toml
options = ["!check"]
