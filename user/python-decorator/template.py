pkgname = "python-decorator"
pkgver = "5.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python library for decorators"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-2-Clause"
url = "https://github.com/micheles/decorator"
source = f"$(PYPI_SITE)/d/decorator/decorator-{pkgver}.tar.gz"
sha256 = "637996211036b6385ef91435e4fae22989472f9d571faba8927ba8253acbc330"


def check(self):
    self.do(
        "python",
        "-m",
        "unittest",
        "discover",
        "-s",
        "src/tests",
        env={"PYTHONPATH": "src"},
    )


def post_install(self):
    self.install_license("LICENSE.txt")
