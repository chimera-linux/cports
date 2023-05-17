pkgname = "gc"
pkgver = "8.2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # static breaks symbol visibility
    "--disable-static", "--enable-cplusplus", "--with-libatomic-ops=none"
]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["linux-headers"]
pkgdesc = "Boehm garbage collector for C/C++"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.hboehm.info/gc"
source = f"https://github.com/ivmai/bdwgc/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "f30107bcb062e0920a790ffffa56d9512348546859364c23a14be264b38836a0"

tool_flags = {
    "CFLAGS": [
        "-D_GNU_SOURCE", "-DNO_GETCONTEXT",
        "-DUSE_MMAP", "-DHAVE_DL_ITERATE_PHDR",
    ]
}

def post_install(self):
    self.install_license("README.QUICK")

@subpackage("gc-devel")
def _devel(self):
    return self.default_devel()
