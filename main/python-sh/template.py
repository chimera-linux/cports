pkgname = "python-sh"
pkgver = "2.2.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://sh.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/s/sh/sh-{pkgver}.tar.gz"
sha256 = "287021ae84183dea49787985e33797dda7fe769e4f95f2c94dff8e245ab4cb00"


def post_install(self):
    self.install_license("LICENSE.txt")
