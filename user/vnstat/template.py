pkgname = "vnstat"
pkgver = "2.13"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf", "automake", "pkgconf"]
makedepends = ["libgd-devel", "sqlite-devel"]
checkdepends = ["check-devel"]
pkgdesc = "Network traffic monitor"
license = "GPL-2.0-or-later"
url = "https://humdi.net/vnstat"
source = f"https://github.com/vergoh/vnstat/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "67a87e05acf09fb5ae368038656000ea50acae789a910b02ad3d3a815e75662c"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.rm(self.destdir / "etc/vnstat.conf")
