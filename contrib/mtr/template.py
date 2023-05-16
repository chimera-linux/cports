pkgname = "mtr"
pkgver = "0.95"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-gtk"]
hostmakedepends = ["automake", "pkgconf", "libcap-progs"]
makedepends = ["ncurses-devel", "libcap-devel"]
depends = ["libcap-progs"]
pkgdesc = "Network diagnostic tool"
maintainer = "eater <=@eater.me>"
license = "GPL-3.0-only AND BSD-3-Clause"
url = "https://www.bitwizard.nl/mtr"
source = f"https://github.com/traviscross/mtr/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "12490fb660ba5fb34df8c06a0f62b4f9cbd11a584fc3f6eceda0a99124e8596f"
# tries to reach the internet
options = ["!check"]

def pre_configure(self):
    self.do("./bootstrap.sh")
