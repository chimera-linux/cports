pkgname = "bash-completion"
pkgver = "2.18.0"
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
sha256 = "88bcf85124f77f74f2f2f8bcd16ac4382d807a827ede742a64940c7116aea33f"
# what's the point (needs a truckload of checkdepends too)
options = ["etcfiles", "!check"]
