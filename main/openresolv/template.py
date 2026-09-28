pkgname = "openresolv"
pkgver = "3.17.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--libexecdir=/usr/lib/resolvconf"]
configure_gen = []
make_dir = "."
pkgdesc = "Management framework for resolv.conf"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/openresolv"
source = f"https://github.com/NetworkConfiguration/openresolv/releases/download/v{pkgver}/openresolv-{pkgver}.tar.xz"
sha256 = "901d83a15520b80e117aeca8cb6f5b70ceb205ba050a638d45cebcf304df729b"
hardening = ["vis", "cfi"]
# no test suite
options = ["etcfiles", "!check"]


def post_install(self):
    self.install_license("LICENSE")
    # rename
    self.rename("usr/bin/resolvconf", "resolvconf-openresolv")
    self.rename("usr/share/man/man8/resolvconf.8", "resolvconf-openresolv.8")
