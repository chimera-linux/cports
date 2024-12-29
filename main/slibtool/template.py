pkgname = "slibtool"
pkgver = "0.6.0"
pkgrel = 2
build_style = "gnu_configure"
configure_gen = []
pkgdesc = "Alternative libtool implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://dev.midipix.org/cross/slibtool"
source = f"https://dl.foss21.org/slibtool/slibtool-{pkgver}.tar.xz"
sha256 = "10b0a12c074b10fa1fec6fe74937b4812c3a7b37f7cc45d0dca68495c2b45e6a"
# no tests?
options = ["!check"]


# custom configure does not understand --sysroot
def configure(self):
    from cbuild.util import gnu_configure

    gnu_configure.configure(self, sysroot=False)


def post_install(self):
    self.install_license("COPYING.SLIBTOOL")
