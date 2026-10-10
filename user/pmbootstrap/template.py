pkgname = "pmbootstrap"
pkgver = "3.12.0"
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
sha256 = "ff75a530246d4810d8929a83056035735d17fc68cb92440eb05e25dd2fc2716f"
