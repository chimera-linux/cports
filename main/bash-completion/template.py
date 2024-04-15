pkgname = "bash-completion"
pkgver = "2.13.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_cmd = "gmake"
make_install_args = [
    "profiledir=/etc/bash/bashrc.d",
    "compatdir=/usr/share/bash-completion/completions",
]
hostmakedepends = ["gmake", "pkgconf"]
checkdepends = ["bash", "python-pytest", "python-pexpect"]
depends = ["bash"]
pkgdesc = "Programmable completion functions for bash"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/scop/bash-completion"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c5f99a39e40f0d154c03ff15438e87ece1f5ac666336a4459899e2ff4bedf3d1"
# what's the point (needs a truckload of checkdepends too)
options = ["!check"]
