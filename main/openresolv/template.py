pkgname = "openresolv"
pkgver = "3.13.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--libexecdir=/usr/libexec/resolvconf"]
make_dir = "."
pkgdesc = "Management framework for resolv.conf"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/openresolv"
source = f"https://github.com/NetworkConfiguration/{pkgname}/archive/refs/tags/{pkgname}-{pkgver}.tar.gz"
sha256 = "799d075542185217dcdaec00f32d7b92000d89029d29e50645a5d2a39736921b"
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
