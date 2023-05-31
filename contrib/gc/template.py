pkgname = "gc"
pkgver = "8.2.4"
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
sha256 = "3d0d3cdbe077403d3106bb40f0cbb563413d6efdbb2a7e1cd6886595dec48fc2"

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
