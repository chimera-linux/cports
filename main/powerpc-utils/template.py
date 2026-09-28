pkgname = "powerpc-utils"
pkgver = "1.3.13"
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
    "linux-headers",
    "numactl-devel",
    "zlib-ng-compat-devel",
]
depends = ["bash"]
pkgdesc = "Suite of utilities for Linux on Power systems"
license = "GPL-2.0-or-later"
url = "https://github.com/ibm-power-utilities/powerpc-utils"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "35efb04063f1b7bd9d715f1d8d3ab75352b595b1fd12349d7570a7ba19ba6d86"
# too many places that use PATH_MAX without limits.h include
tool_flags = {"CFLAGS": ["-DPATH_MAX=4096"]}
