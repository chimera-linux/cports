pkgname = "bash-completion"
pkgver = "2.15.0"
pkgrel = 0
build_style = "gnu_configure"
make_install_args = [
    "profiledir=/etc/bash/bashrc.d",
]
hostmakedepends = ["automake", "pkgconf"]
checkdepends = ["bash", "python-pytest", "python-pexpect"]
depends = ["bash"]
pkgdesc = "Programmable completion functions for bash"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/scop/bash-completion"
source = f"{url}/releases/download/{pkgver}/bash-completion-{pkgver}.tar.xz"
sha256 = "976a62ee6226970283cda85ecb9c7a4a88f62574c0a6f9e856126976decf1a06"
# what's the point (needs a truckload of checkdepends too)
options = ["!check"]
