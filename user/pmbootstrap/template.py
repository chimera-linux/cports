pkgname = "pmbootstrap"
pkgver = "3.7.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "git",
    "kpartx",
    "procps",
    "util-linux-mount",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Sophisticated tool to develop and install postmarketOS"
license = "GPL-3.0-or-later"
url = "https://gitlab.postmarketos.org/postmarketOS/pmbootstrap"
source = f"{url}/-/archive/{pkgver}/pmbootstrap-{pkgver}.tar.gz"
sha256 = "49cce086bc63c2c5ecf95f58f765b66d8e1127e38be3a68a97443dc30b92dcbd"
# Tests require to git clone etc.
options = ["!check"]
