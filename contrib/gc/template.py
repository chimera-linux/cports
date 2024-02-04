pkgname = "gc"
pkgver = "8.2.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # static breaks symbol visibility
    "--disable-static",
    "--enable-cplusplus",
    "--with-libatomic-ops=none",
]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake", "automake", "libtool"]
makedepends = ["linux-headers"]
pkgdesc = "Boehm garbage collector for C/C++"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.hboehm.info/gc"
source = f"https://github.com/ivmai/bdwgc/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "b9183fe49d4c44c7327992f626f8eaa1d8b14de140f243edb1c9dcff7719a7fc"

tool_flags = {
    "CFLAGS": [
        "-D_GNU_SOURCE",
        "-DNO_GETCONTEXT",
        "-DUSE_MMAP",
        "-DHAVE_DL_ITERATE_PHDR",
    ]
}


def post_install(self):
    self.install_license("README.QUICK")


@subpackage("gc-devel")
def _devel(self):
    return self.default_devel()
