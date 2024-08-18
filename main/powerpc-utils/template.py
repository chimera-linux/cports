pkgname = "powerpc-utils"
pkgver = "1.3.12"
pkgrel = 0
archs = ["ppc*"]
build_style = "gnu_configure"
configure_args = [
    "--disable-werror",
    "--with-librtas",
    "ac_cv_lib_rtasevent_parse_rtas_event=yes",
]
configure_gen = ["./autogen.sh"]
hostmakedepends = ["automake", "libtool"]
makedepends = [
    "librtas-devel",
    "zlib-ng-compat-devel",
    "libnuma-devel",
    "linux-headers",
]
depends = ["bash"]
pkgdesc = "Suite of utilities for Linux on Power systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/ibm-power-utilities/powerpc-utils"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "c3f62f63fb856bbd70eee997ecd3d870eca2220103fbf00d8e3d7ee414f5c7e7"
# too many places that use PATH_MAX without limits.h include
tool_flags = {"CFLAGS": ["-DPATH_MAX=4096"]}
