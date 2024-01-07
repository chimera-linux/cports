pkgname = "bash-completion"
pkgver = "2.11"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_install_args = ["profiledir=/etc/bash/bashrc.d"]
hostmakedepends = ["gmake", "pkgconf"]
checkdepends = ["bash", "python-pytest", "python-pexpect"]
depends = ["bash"]
pkgdesc = "Programmable completion functions for bash"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/scop/bash-completion"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "73a8894bad94dee83ab468fa09f628daffd567e8bef1a24277f1e9a0daf911ac"
# missing checkdepends
options = ["!check"]

configure_gen = []
