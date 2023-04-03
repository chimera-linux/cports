pkgname = "openresolv"
pkgver = "3.12.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--libexecdir=/usr/libexec/resolvconf"]
make_dir = "."
pkgdesc = "Management framework for resolv.conf"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/openresolv"
source = f"https://roy.marples.name/downloads/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "42b30508e857a228535c631eaac936862d86eca68c14b5c0bf387ba176b91b97"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
    # rename
    self.mv(
        self.destdir / "usr/bin/resolvconf",
        self.destdir / "usr/bin/resolvconf-openresolv"
    )
    self.mv(
        self.destdir / "usr/share/man/man8/resolvconf.8",
        self.destdir / "usr/share/man/man8/resolvconf-openresolv.8"
    )
