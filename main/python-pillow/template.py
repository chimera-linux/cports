pkgname = "python-pillow"
pkgver = "12.2.0"
pkgrel = 0
build_style = "python_pep517"
make_check_target = "Tests"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = [
    "freetype-devel",
    "lcms2-devel",
    "libavif-devel",
    "libjpeg-turbo-devel",
    "libtiff-devel",
    "libwebp-devel",
    "openjpeg-devel",
    "python-devel",
    "python-pybind11-devel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python Imaging Library"
license = "MIT-CMU"
url = "https://python-pillow.org"
source = f"$(PYPI_SITE)/p/pillow/pillow-{pkgver}.tar.gz"
sha256 = "a830b1a40919539d07806aa58e1b114df53ddd43213d9c8b75847eee6c0182b5"


def post_install(self):
    self.install_license("LICENSE")
