pkgname = "python-pillow"
pkgver = "10.3.0"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "Tests"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = [
    "freetype-devel",
    "lcms2-devel",
    "libjpeg-turbo-devel",
    "libtiff-devel",
    "libwebp-devel",
    "openjpeg-devel",
    "python-devel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python Imaging Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:PIL"
url = "https://python-pillow.org"
source = f"$(PYPI_SITE)/p/pillow/pillow-{pkgver}.tar.gz"
sha256 = "9d2455fbf44c914840c793e89aa82d0e1763a14253a000743719ae5946814b2d"


def post_install(self):
    self.install_license("LICENSE")
