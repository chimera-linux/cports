pkgname = "python-pillow"
pkgver = "11.2.1"
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
    "libjpeg-turbo-devel",
    "libtiff-devel",
    "libwebp-devel",
    "openjpeg-devel",
    "python-devel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python Imaging Library"
license = "MIT-CMU"
url = "https://python-pillow.org"
source = f"$(PYPI_SITE)/p/pillow/pillow-{pkgver}.tar.gz"
sha256 = "a64dd61998416367b7ef979b73d3a85853ba9bec4c2925f74e588879a58716b6"


def post_install(self):
    self.install_license("LICENSE")
