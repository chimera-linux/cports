pkgname = "mtr"
pkgver = "0.95"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--without-gtk"]
configure_gen = ["./bootstrap.sh"]
hostmakedepends = ["automake", "pkgconf", "libcap-progs"]
makedepends = ["ncurses-devel", "libcap-devel"]
pkgdesc = "Network diagnostic tool"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-only AND BSD-3-Clause"
url = "https://www.bitwizard.nl/mtr"
source = f"https://github.com/traviscross/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "12490fb660ba5fb34df8c06a0f62b4f9cbd11a584fc3f6eceda0a99124e8596f"
file_xattrs = {
    "usr/bin/mtr-packet": {
        "security.capability": "cap_net_raw+ep",
    },
}
# tries to reach the internet
options = ["!check"]


def post_install(self):
    self.install_license("BSDCOPYING")
