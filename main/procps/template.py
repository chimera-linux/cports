pkgname = "procps"
pkgver = "4.0.5"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.com/procps-ng/procps"
source = f"$(SOURCEFORGE_SITE)/procps-ng/Production/procps-ng-{pkgver}.tar.xz"
sha256 = "c2e6d193cc78f84cd6ddb72aaf6d5c6a9162f0470e5992092057f5ff518562fa"
hardening = ["!vis", "!cfi"]
# dejagnu
options = ["!check"]


def post_install(self):
    self.install_file(self.files_path / "sysctl.conf", "etc")


@subpackage("procps-devel")
def _(self):
    return self.default_devel()
