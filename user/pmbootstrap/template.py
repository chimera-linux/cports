pkgname = "pmbootstrap"
pkgver = "3.12.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
checkdepends = ["git", "kpartx", "procps", "python-pytest", "util-linux-mount"]
depends = ["android-tools"]
pkgdesc = "Sophisticated chroot/build/flash tool to develop and install Nura"
license = "GPL-3.0-or-later"
url = "https://gitlab.postmarketos.org/postmarketOS/pmbootstrap"
source = f"{url}/-/archive/{pkgver}/pmbootstrap-{pkgver}.tar.bz2"
sha256 = "7c6dd73d4ccda000b611d3756e9a4110c023abd745ee20c0137cfb9ffc7507e7"
