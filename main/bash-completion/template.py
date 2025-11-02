pkgname = "bash-completion"
pkgver = "2.17.0"
pkgrel = 0
build_style = "gnu_configure"
make_install_args = [
    "profiledir=/usr/share/bash/bashrc.d",
]
hostmakedepends = ["automake", "pkgconf"]
checkdepends = ["bash", "python-pytest", "python-pexpect"]
depends = ["bash"]
pkgdesc = "Programmable completion functions for bash"
license = "GPL-2.0-or-later"
url = "https://github.com/scop/bash-completion"
source = f"{url}/releases/download/{pkgver}/bash-completion-{pkgver}.tar.xz"
sha256 = "dd9d825e496435fb3beba3ae7bea9f77e821e894667d07431d1d4c8c570b9e58"
# what's the point (needs a truckload of checkdepends too)
options = ["!check"]
