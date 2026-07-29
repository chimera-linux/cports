pkgname = "python-anyio"
pkgver = "4.14.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
    "python-wheel",
]
depends = [
    "python",
    "python-idna",
    "python-sniffio",
    "python-typing_extensions",
]
pkgdesc = "High-level asynchronous concurrency and networking framework"
license = "MIT"
url = "https://anyio.readthedocs.io"
source = f"https://pypi.io/packages/source/a/anyio/anyio-{pkgver}.tar.gz"
sha256 = "cfa139f3ed1a23ee8f88a145ddb5ac7605b8bbfd8592baacd7ce3d8bb4313c7f"
# tests require psutil, pytest-mock, trustme...etc, which are not packaged; skip for now
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
