pkgname = "python-decorator"
pkgver = "5.2.1"
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
license = "BSD-2-Clause"
url = "https://github.com/micheles/decorator"
source = f"$(PYPI_SITE)/d/decorator/decorator-{pkgver}.tar.gz"
sha256 = "65f266143752f734b0a7cc83c46f4618af75b8c5911b00ccb61d0ac9b6da0360"


def check(self):
    self.do(
        "python",
        "-m",
        "unittest",
        "discover",
        "-s",
        "tests",
        env={"PYTHONPATH": "src"},
    )


def post_install(self):
    self.install_license("LICENSE.txt")
