pkgname = "limitcpu"
pkgver = "3.2"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Throttle the CPU cycles used by a program"
license = "GPL-2.0-or-later"
url = "https://limitcpu.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/limitcpu/cpulimit-{pkgver}.tar.gz"
sha256 = "59ffeb1a3517afe45998714be8419260a43632f7cec08f0b026c1eccdff57cfc"
hardening = ["vis", "cfi"]
# has no tests intended to be used for automation
options = ["!check"]


def install(self):
    self.make.install([f"PREFIX={self.chroot_destdir}/usr"])
    self.install_license("LICENSE")
