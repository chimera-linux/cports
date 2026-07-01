pkgname = "procps"
pkgver = "4.0.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-kill",
    "--enable-watch8bit",
    "--disable-modern-top",
    "--without-systemd",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
]
makedepends = ["ncurses-devel"]
pkgdesc = "Utilities for monitoring your system and its processes"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.com/procps-ng/procps"
source = f"$(SOURCEFORGE_SITE)/procps-ng/Production/procps-ng-{pkgver}.tar.xz"
sha256 = "67bea6fbc3a42a535a0230c9e891e5ddfb4d9d39422d46565a2990d1ace15216"
hardening = ["!vis", "!cfi"]
# dejagnu
options = ["etcfiles", "!check"]


def post_install(self):
    self.install_file(self.files_path / "sysctl.conf", "etc")


@subpackage("procps-devel")
def _(self):
    return self.default_devel()
