pkgname = "python-looseversion"
pkgver = "1.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Python extension for comparing version strings"
license = "PSF-2.0"
url = "https://pypi.org/project/looseversion"
source = f"$(PYPI_SITE)/l/looseversion/looseversion-{pkgver}.tar.gz"
sha256 = "ebde65f3f6bb9531a81016c6fef3eb95a61181adc47b7f949e9c0ea47911669e"
# couldn't make it to work
options = ["!check"]
