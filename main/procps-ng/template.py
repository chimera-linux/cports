pkgname = "procps-ng"
pkgver = "3.3.17"
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
source = f"$(SOURCEFORGE_SITE)/{pkgname}/Production/{pkgname}-{pkgver}.tar.xz"
sha256 = "4518b3e7aafd34ec07d0063d250fd474999b20b200218c3ae56f5d2113f141b4"
hardening = ["!cfi"] # TODO

def post_install(self):
    self.install_file(self.files_path / "sysctl.conf", "etc")

@subpackage("procps-ng-devel")
def _devel(self):
    return self.default_devel()
