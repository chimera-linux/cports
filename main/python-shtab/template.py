pkgname = "python-shtab"
pkgver = "1.7.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["bash", "python-pytest"]
pkgdesc = "Shell completion generation for Python CLI applications"
maintainer = "triallax <triallax@tutanota.com>"
license = "Apache-2.0"
url = "https://docs.iterative.ai/shtab"
source = f"$(PYPI_SITE)/s/shtab/shtab-{pkgver}.tar.gz"
sha256 = "4e4bcb02eeb82ec45920a5d0add92eac9c9b63b2804c9196c1f1fdc2d039243c"
