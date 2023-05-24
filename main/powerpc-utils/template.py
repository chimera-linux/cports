pkgname = "powerpc-utils"
pkgver = "1.3.11"
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
    "zlib-devel",
    "libnuma-devel",
    "linux-headers",
]
pkgdesc = "Suite of utilities for Linux on Power systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/ibm-power-utilities/powerpc-utils"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6bb16078068d8b889afdd78927d2f061702ef155e57fc548ae573e2b0b90ca13"
# too many places that use PATH_MAX without limits.h include
tool_flags = {"CFLAGS": ["-DPATH_MAX=4096"]}
