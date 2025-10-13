pkgname = "slibtool"
pkgver = "0.7.4"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
pkgdesc = "Alternative libtool implementation"
license = "MIT"
url = "https://dev.midipix.org/cross/slibtool"
source = f"https://dl.foss21.org/slibtool/slibtool-{pkgver}.tar.xz"
sha256 = "2e7a4ae528c49c82743ae91260d3fa24bee3d91d9a87066e3491a24ba745a948"
# no tests?
options = ["!check"]


# custom configure does not understand --sysroot
def configure(self):
    from cbuild.util import gnu_configure

    gnu_configure.configure(self, sysroot=False)


def post_install(self):
    self.install_license("COPYING.SLIBTOOL")
