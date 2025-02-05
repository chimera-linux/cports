pkgname = "iputils"
pkgver = "20240905"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-DNO_SETCAP_OR_SUID=true",
    "-DUSE_IDN=false",
]
hostmakedepends = [
    "docbook-xsl",
    "iproute2",
    "libcap-progs",
    "meson",
    "pkgconf",
    "libxslt-progs",
]
makedepends = ["libcap-devel"]
pkgdesc = "Useful utilities for Linux networking"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND GPL-2.0-or-later"
url = "https://github.com/iputils/iputils"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "055b4e6e4f298c97fd5848898099e59b4590db63fac3f7ad4fa796354ad44403"
file_modes = {
    "usr/bin/clockdiff": ("root", "root", 0o755),
    "usr/bin/ping": ("root", "root", 0o755),
}
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
