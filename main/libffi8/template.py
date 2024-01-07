pkgname = "libffi8"
pkgver = "3.4.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--includedir=/usr/include",
    "--disable-multi-os-directory",
    "--with-pic",
    # https://github.com/libffi/libffi/pull/647
    # some stuff (notably gobject-introspection) uses
    # libffi incorrectly, prevent them from being broken for now
    "--disable-exec-static-tramp",
]
hostmakedepends = ["pkgconf"]
# actually only on x86 and arm (tramp.c code) but it does not hurt
makedepends = ["linux-headers"]
checkdepends = ["dejagnu"]
pkgdesc = "Library supporting Foreign Function Interfaces"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://sourceware.org/libffi"
source = f"https://github.com/libffi/libffi/releases/download/v{pkgver}/libffi-{pkgver}.tar.gz"
sha256 = "d66c56ad259a82cf2a9dfc408b32bf5da52371500b84745f7fb8b645712df676"
# loop: automake -> autoconf -> chimerautils -> meson -> python ->
# libffi -> dejagnu -> expect -> automake
options = ["!check", "linkundefver"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libffi-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/info"])


configure_gen = []
