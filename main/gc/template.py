pkgname = "gc"
pkgver = "8.2.8"
pkgrel = 1
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.hboehm.info/gc"
source = f"https://github.com/ivmai/bdwgc/releases/download/v{pkgver}/gc-{pkgver}.tar.gz"
sha256 = "7649020621cb26325e1fb5c8742590d92fb48ce5c259b502faf7d9fb5dabb160"
patch_style = "patch"


def post_install(self):
    self.install_license("README.QUICK")


@subpackage("gc-devel")
def _(self):
    return self.default_devel()
