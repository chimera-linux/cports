pkgname = "python-lxns"
pkgver = "0.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-meson",
    "python-installer",
]
makedepends = ["linux-headers", "python-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Python library to control Linux kernel namespaces"
maintainer = "ttyyls <contact@behri.org>"
license = "MPL-2.0"
url = "https://github.com/igo95862/python-lxns"
source = f"$(PYPI_SITE)/l/lxns/lxns-{pkgver}.tar.gz"
sha256 = "7913255a5e8146e9950ee8bcd60b25ac62c9ed289eecd3b394d2aa60e09003b2"
