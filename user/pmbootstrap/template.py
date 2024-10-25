pkgname = "pmbootstrap"
pkgver = "2.3.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-setuptools",
    "python-installer",
]
checkdepends = ["python-pytest"]
depends = ["android-tools"]
pkgdesc = "Chroot/build/flash tool to develop and install postmarketOS"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/postmarketOS/pmbootstrap"
source = f"{url}/-/archive/{pkgver}/pmbootstrap-{pkgver}.tar.gz"
sha256 = "aba09c0a27918dac4b07641339ccf86e6ec0d14d4602056dac44ec49af12c894"
# check: requires networking
options = ["!check"]
