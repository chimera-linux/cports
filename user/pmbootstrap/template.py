pkgname = "pmbootstrap"
pkgver = "3.6.0"
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
sha256 = "8394bd77a86b3ff8a49a3898a8b5fba835a96da99a0733dd9a702210dbac546b"
# Tests require to git clone etc.
options = ["!check"]
