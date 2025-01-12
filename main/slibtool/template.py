pkgname = "slibtool"
pkgver = "0.6.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
pkgdesc = "Alternative libtool implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://dev.midipix.org/cross/slibtool"
source = f"https://dl.foss21.org/slibtool/slibtool-{pkgver}.tar.xz"
sha256 = "61b07f9f371ca05dc5b1259b27e73d8d7a2ef15e2a6adc9bac9816c5a4beacc4"
# no tests?
options = ["!check"]


# custom configure does not understand --sysroot
def configure(self):
    from cbuild.util import gnu_configure

    gnu_configure.configure(self, sysroot=False)


def post_install(self):
    self.install_license("COPYING.SLIBTOOL")
