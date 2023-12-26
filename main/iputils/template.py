pkgname = "iputils"
pkgver = "20231222"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-DNO_SETCAP_OR_SUID=true",
    "-DUSE_IDN=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "xsltproc",
    "docbook-xsl",
    "libcap-progs",
    "iproute2",
]
makedepends = ["libcap-devel"]
pkgdesc = "Useful utilities for Linux networking"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND GPL-2.0-or-later"
url = "https://github.com/iputils/iputils"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "18d51e7b416da0ecbc0ae18a2cba76407ca0b5b3f32c356034f258a0cb56793f"
file_xattrs = {
    "usr/bin/clockdiff": {
        "security.capability": "cap_net_raw,cap_sys_nice+ep",
    },
    "usr/bin/ping": {"security.capability": "cap_net_raw+p"},
}
hardening = ["vis", "cfi"]
# operation not permitted (sandbox, unshared network)
options = ["!check"]


def post_install(self):
    self.install_license("Documentation/LICENSE.BSD3")
