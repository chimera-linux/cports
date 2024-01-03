pkgname = "chkrootkit"
pkgver = "0.58"
_pkgver = f"{pkgver}b-1"
pkgrel = 0
build_style = "makefile"
makedepends = [
    "libatomic-chimera-devel-static",
    "libunwind-devel-static",
    "linux-headers",
    "musl-devel-static",
]
depends = ["iproute2"]
pkgdesc = "Locally checks for signs of a rootkit"
maintainer = "Froggo <froggo8311@proton.me>"
license = "custom:chkrootkit"
url = "https://salsa.debian.org/pkg-security-team/chkrootkit"
source = f"{url}/-/archive/debian/{_pkgver}/chkrootkit-debian-{_pkgver}.tar.gz"
sha256 = "f307107cd2005014085710e69a523c98bccac5ef2714627aff09fbb0d451ee6c"
# disable tests
options = ["!check"]


def do_install(self):
    self.install_license("COPYRIGHT")
    for file in (
        "check_wtmpx",
        "chkdirs",
        "chklastlog",
        "chkproc",
        "chkrootkit",
        "chkutmp",
        "chkwtmp",
        "ifpromisc",
        "strings-static",
    ):
        self.install_bin(file)
