pkgname = "procps"
pkgver = "4.0.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-kill", "--enable-watch8bit", "--disable-modern-top",
    "--without-systemd",
]
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["ncurses-devel"]
checkdepends = ["dejagnu"]
pkgdesc = "Utilities for monitoring your system and its processes"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.com/procps-ng/procps"
source = f"$(SOURCEFORGE_SITE)/procps-ng/Production/procps-ng-{pkgver}.tar.xz"
sha256 = "303c8ec4f96ae18d8eaef86c2bd0986938764a45dc505fe0a0af868c674dba92"
hardening = ["!cfi"] # TODO

def post_install(self):
    self.install_file(self.files_path / "sysctl.conf", "etc")

@subpackage("procps-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
