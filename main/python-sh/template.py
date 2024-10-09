pkgname = "python-sh"
pkgver = "2.1.0"
pkgrel = 0
build_style = "python_pep517"
# checks if the return code of `ls` for non-existent dir is '1' on macos and '2'
# otherwise, and it's 1 for us since we use freebsd ls.
# posix just says >0, useless test
make_check_args = ["-k", "not test_ok_code"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python subprocess replacement module"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://sh.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/s/sh/sh-{pkgver}.tar.gz"
sha256 = "7e27301c574bec8ca5bf6f211851357526455ee97cd27a7c4c6cc5e2375399cb"


def post_install(self):
    self.install_license("LICENSE.txt")
