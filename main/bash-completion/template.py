pkgname = "bash-completion"
pkgver = "2.14.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_cmd = "gmake"
make_install_args = [
    "compatdir=/usr/share/bash-completion/completions",
    "profiledir=/etc/bash/bashrc.d",
]
hostmakedepends = ["gmake", "pkgconf"]
checkdepends = ["bash", "python-pytest", "python-pexpect"]
depends = ["bash"]
pkgdesc = "Programmable completion functions for bash"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/scop/bash-completion"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "5c7494f968280832d6adb5aa19f745a56f1a79df311e59338c5efa6f7285e168"
# what's the point (needs a truckload of checkdepends too)
options = ["!check"]
