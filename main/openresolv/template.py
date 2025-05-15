pkgname = "openresolv"
pkgver = "3.16.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--libexecdir=/usr/libexec/resolvconf"]
configure_gen = []
make_dir = "."
pkgdesc = "Management framework for resolv.conf"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/openresolv"
source = f"https://github.com/NetworkConfiguration/openresolv/releases/download/v{pkgver}/openresolv-{pkgver}.tar.xz"
sha256 = "389cb94b57dca1e39a501c95efd448452adffbf311bb8a3bebd39f7f202ac284"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    # rename
    self.rename("usr/bin/resolvconf", "resolvconf-openresolv")
    self.rename("usr/share/man/man8/resolvconf.8", "resolvconf-openresolv.8")
