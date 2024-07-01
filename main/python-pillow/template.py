pkgname = "python-pillow"
pkgver = "10.4.0"
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
license = "MIT-CMU"
url = "https://python-pillow.org"
source = f"$(PYPI_SITE)/p/pillow/pillow-{pkgver}.tar.gz"
sha256 = "166c1cd4d24309b30d61f79f4a9114b7b2313d7450912277855ff5dfd7cd4a06"


def post_install(self):
    self.install_license("LICENSE")
