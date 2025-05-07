pkgname = "python-pyzmq"
pkgver = "26.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "ninja",
    "pkgconf",
    "python-build",
    "python-cython",
    "python-installer",
    "python-scikit_build_core",
    "python-setuptools",
]
makedepends = ["python-devel", "zeromq-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Python bindings for ZeroMQ"
license = "BSD-3-Clause"
url = "https://pypi.org/project/pyzmq"
source = f"$(PYPI_SITE)/p/pyzmq/pyzmq-{pkgver}.tar.gz"
sha256 = "4bd13f85f80962f91a651a7356fe0472791a5f7a92f227822b5acf44795c626d"
# couldn't make it work
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
