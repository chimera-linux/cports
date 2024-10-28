pkgname = "python-pyte"
pkgver = "0.8.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-wcwidth"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "In-memory terminal emulator library"
maintainer = "triallax <triallax@tutanota.com>"
# Doesn't seem to be specified anywhere, presume -only
license = "LGPL-3.0-only"
url = "https://pyte.readthedocs.org"
source = f"$(PYPI_SITE)/p/pyte/pyte-{pkgver}.tar.gz"
sha256 = "5af970e843fa96a97149d64e170c984721f20e52227a2f57f0a54207f08f083f"
