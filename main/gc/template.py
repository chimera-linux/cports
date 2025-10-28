pkgname = "gc"
pkgver = "8.2.10"
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
sha256 = "832cf4f7cf676b59582ed3b1bbd90a8d0e0ddbc3b11cb3b2096c5177ce39cc47"


def post_install(self):
    self.install_license("README.QUICK")


@subpackage("gc-devel")
def _(self):
    return self.default_devel()
