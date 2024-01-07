pkgname = "extrace"
pkgver = "0.9"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["libcap-progs"]
makedepends = ["linux-headers"]
pkgdesc = "Trace program executions occurring on a system"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later AND BSD-2-Clause"
url = "https://github.com/leahneukirchen/extrace"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e488db1126bd941e5a094e6024c3975f70abfa7ad51a3451191d1518c0b35ced"
file_xattrs = {
    "usr/bin/extrace": {
        "security.capability": "cap_net_admin+ep",
    },
    "usr/bin/pwait": {
        "security.capability": "cap_net_admin+ep",
    },
}
hardening = ["vis", "cfi"]
# No tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
