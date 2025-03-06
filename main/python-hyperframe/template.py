pkgname = "python-hyperframe"
pkgver = "6.1.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python implementation of HTTP/2 framing"
license = "MIT"
url = "https://github.com/python-hyper/hyperframe"
source = f"$(PYPI_SITE)/h/hyperframe/hyperframe-{pkgver}.tar.gz"
sha256 = "f630908a00854a7adeabd6382b43923a4c4cd4b821fcb527e6ab9e15382a3b08"
# fails to find itself?
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
