pkgname = "iputils"
pkgver = "20250605"
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
    "libxslt-progs",
    "meson",
    "pkgconf",
]
makedepends = ["libcap-devel"]
pkgdesc = "Useful utilities for Linux networking"
license = "BSD-3-Clause AND GPL-2.0-or-later"
url = "https://github.com/iputils/iputils"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "19e680c9eef8c079da4da37040b5f5453763205b4edfb1e2c114de77908927e4"
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
