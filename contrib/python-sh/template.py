pkgname = "python-sh"
pkgver = "2.0.7"
pkgrel = 1
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
sha256 = "029d45198902bfb967391eccfd13a88d92f7cebd200411e93f99ebacc6afbb35"


def post_install(self):
    self.install_license("LICENSE.txt")
