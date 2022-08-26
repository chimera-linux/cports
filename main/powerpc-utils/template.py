pkgname = "powerpc-utils"
pkgver = "1.3.10"
pkgrel = 0
archs = ["ppc*"]
build_style = "gnu_configure"
configure_args = [
    "--disable-werror", "--with-librtas",
    "ac_cv_lib_rtasevent_parse_rtas_event=yes",
    "LIBS=-lexecinfo",
]
hostmakedepends = ["automake", "libtool"]
makedepends = [
    "librtas-devel", "zlib-devel", "libexecinfo-devel", "libnuma-devel",
    "linux-headers",
]
pkgdesc = "Suite of utilities for Linux on Power systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/ibm-power-utilities/powerpc-utils"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d64d9016a3e63a1e44c6e0833742cf964ae6bb1c6a9c7f0c7c5748aa335dc3db"
# too many places that use PATH_MAX without limits.h include
tool_flags = {"CFLAGS": ["-DPATH_MAX=4096"]}

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")
