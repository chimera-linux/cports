pkgname = "vnstat"
pkgver = "2.14"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf", "automake", "pkgconf"]
makedepends = ["dinit-chimera", "libgd-devel", "sqlite-devel"]
checkdepends = ["check-devel"]
pkgdesc = "Network traffic monitor"
license = "GPL-2.0-or-later"
url = "https://humdi.net/vnstat"
source = f"https://github.com/vergoh/vnstat/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "da6ca8105fbdca42290ac36c4f01314709b959b798bddcd9227ea25bf60c187f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "vnstatd")
    self.install_file("cfg/vnstat.conf", "usr/share/examples/vnstat")
    self.uninstall("etc")
