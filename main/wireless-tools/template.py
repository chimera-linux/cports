pkgname = "wireless-tools"
pkgver = "30_pre9"
pkgrel = 1
build_style = "makefile"
makedepends = ["linux-headers"]
pkgdesc = "Wireless extension manipulation tools"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-only"
url = "https://hewlettpackard.github.io/wireless-tools/Tools.html"
source = f"https://hewlettpackard.github.io/wireless-tools/wireless_tools.{pkgver.replace('_', '.')}.tar.gz"
sha256 = "abd9c5c98abf1fdd11892ac2f8a56737544fe101e1be27c6241a564948f34c63"
# No tests
options = ["!check"]


def init_install(self):
    self.make_install_args += [
        f"INSTALL_DIR={self.chroot_destdir}/usr/bin",
        f"INSTALL_LIB={self.chroot_destdir}/usr/lib",
        f"INSTALL_INC={self.chroot_destdir}/usr/include",
        f"INSTALL_MAN={self.chroot_destdir}/usr/share/man",
    ]


@subpackage("wireless-tools-devel")
def _(self):
    self.depends += ["linux-headers"]
    return self.default_devel()
