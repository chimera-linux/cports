pkgname = "python-idna"
pkgver = "3.4"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "tests"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-flit_core",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Internationalized Domain Names in Applications (IDNA) for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/kjd/idna"
source = f"$(PYPI_SITE)/i/idna/idna-{pkgver}.tar.gz"
sha256 = "814f528e8dead7d329833b91c5faa87d60bf71824cd12a7530b5526063d02cb4"
# dep cycle with pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
