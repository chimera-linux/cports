pkgname = "gc"
pkgver = "8.2.12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # static breaks symbol visibility
    "--disable-static",
    "--enable-cplusplus",
    "--with-libatomic-ops=none",
]
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = ["linux-headers"]
pkgdesc = "Boehm garbage collector for C/C++"
license = "MIT"
url = "https://www.hboehm.info/gc"
source = f"https://github.com/ivmai/bdwgc/releases/download/v{pkgver}/gc-{pkgver}.tar.gz"
sha256 = "42e5194ad06ab6ffb806c83eb99c03462b495d979cda782f3c72c08af833cd4e"


def post_install(self):
    self.install_license("README.QUICK")


@subpackage("gc-devel")
def _(self):
    return self.default_devel()
