pkgname = "python-html5lib"
pkgver = "1.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-six",
    "python-webencodings",
]
checkdepends = [
    "python-mock",
    "python-pytest",
    "python-pytest-expect",
    *depends,
]
pkgdesc = "Python html parser"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/html5lib/html5lib-python"
source = f"$(PYPI_SITE)/h/html5lib/html5lib-{pkgver}.tar.gz"
sha256 = "b2e5b40261e20f354d198eae92afc10d750afb487ed5e50f9c4eaf07c184146f"
# broken with new pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
