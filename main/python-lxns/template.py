pkgname = "python-lxns"
pkgver = "0.1.0"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-meson",
]
makedepends = ["linux-headers", "python-devel"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python library to control Linux kernel namespaces"
license = "MPL-2.0"
url = "https://github.com/igo95862/python-lxns"
source = f"$(PYPI_SITE)/l/lxns/lxns-{pkgver}.tar.gz"
sha256 = "7913255a5e8146e9950ee8bcd60b25ac62c9ed289eecd3b394d2aa60e09003b2"
