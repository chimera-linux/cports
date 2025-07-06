pkgname = "python-pika"
pkgver = "1.3.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = [
    "python-pytest",
    "python-mock",
]
pkgdesc = "Pika Python AMQP Client Library"
license = "BSD-3-Clause"
url = "https://github.com/pika/pika"
source = f"$(PYPI_SITE)/p/pika/pika-{pkgver}.tar.gz"
sha256 = "b2a327ddddf8570b4965b3576ac77091b850262d34ce8c1d8cb4e4146aa4145f"
# unpackaged deps
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
