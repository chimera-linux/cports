pkgname = "mtr"
pkgver = "0.96"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-gtk"]
configure_gen = ["./bootstrap.sh"]
hostmakedepends = ["automake", "pkgconf", "libcap-progs"]
makedepends = ["ncurses-devel", "libcap-devel"]
pkgdesc = "Network diagnostic tool"
license = "GPL-3.0-only AND BSD-3-Clause"
url = "https://www.bitwizard.nl/mtr"
source = (
    f"https://github.com/traviscross/mtr/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "73e6aef3fb6c8b482acb5b5e2b8fa7794045c4f2420276f035ce76c5beae632d"
file_modes = {
    "usr/bin/mtr-packet": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/mtr-packet": {
        "security.capability": "cap_net_raw+ep",
    },
}
# tries to reach the internet
options = ["!check"]


def post_install(self):
    self.install_license("BSDCOPYING")
