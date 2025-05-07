pkgname = "openresolv"
pkgver = "3.16.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--libexecdir=/usr/libexec/resolvconf"]
configure_gen = []
make_dir = "."
pkgdesc = "Management framework for resolv.conf"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/openresolv"
source = f"https://github.com/NetworkConfiguration/openresolv/releases/download/v{pkgver}/openresolv-{pkgver}.tar.xz"
sha256 = "17d8486e53931b00cb06673cfeb038de12636eff59ead79f29379d036cfb6eb5"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    # rename
    self.rename("usr/bin/resolvconf", "resolvconf-openresolv")
    self.rename("usr/share/man/man8/resolvconf.8", "resolvconf-openresolv.8")
