pkgname = "python-random2"
pkgver = "1.0.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Python3-compatible Python2 random module"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "PSF-2.0"
url = "https://pypi.org/project/random2"
source = f"$(PYPI_SITE)/r/random2/random2-{pkgver}.tar.gz"
sha256 = "3754fcef48267567cd5705fa7da6bbc3809cb3f808740313e6705acc3c057e77"


def check(self):
    self.do("python", "src/tests.py")
