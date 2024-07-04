pkgname = "python-hyperlink"
pkgver = "21.0.0"
pkgrel = 2
build_style = "python_pep517"
make_check_target = "build"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-idna"]
checkdepends = ["python-pytest", "python-idna"]
pkgdesc = "Python immutable URLs"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/python-hyper/hyperlink"
source = f"$(PYPI_SITE)/h/hyperlink/hyperlink-{pkgver}.tar.gz"
sha256 = "427af957daa58bc909471c6c40f74c5450fa123dd093fc53efd2e91d2705a56b"


def post_install(self):
    self.install_license("LICENSE")
    # remove tests
    self.uninstall("usr/lib/python*/site-packages/hyperlink/test", glob=True)
