pkgname = "python-aspectlib"
pkgver = "2.0.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = ["-W", "ignore::DeprecationWarning"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-process-tests", "python-pytest", "python-tornado"]
pkgdesc = "Library for quickly writing configurable applications and daemons"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "BSD-2-Clause"
url = "https://github.com/ionelmc/python-pygaljs"
source = f"$(PYPI_SITE)/a/aspectlib/aspectlib-{pkgver}.tar.gz"
sha256 = "a4b461b9da0b531aebcb93efcde3de808a72c60226dd8d902c467d13faf7ce92"


def post_install(self):
    self.install_license("LICENSE")
