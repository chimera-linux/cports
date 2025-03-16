pkgname = "python-sh"
pkgver = "2.2.2"
pkgrel = 1
build_style = "python_pep517"
# checks if the return code of `ls` for non-existent dir is '1' on macos and '2'
# otherwise, and it's 1 for us since we use freebsd ls.
# posix just says >0, useless test
# the latter times out on riscv
make_check_args = [
    "-k",
    "not test_ok_code and not test_done_callback_no_deadlock",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Python subprocess replacement module"
license = "MIT"
url = "https://sh.readthedocs.io/en/latest"
source = f"$(PYPI_SITE)/s/sh/sh-{pkgver}.tar.gz"
sha256 = "653227a7c41a284ec5302173fbc044ee817c7bad5e6e4d8d55741b9aeb9eb65b"


def post_install(self):
    self.install_license("LICENSE.txt")
