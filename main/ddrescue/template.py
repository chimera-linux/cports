pkgname = "ddrescue"
pkgver = "1.30"
pkgrel = 0
build_style = "gnu_configure"
# handrolled conf
configure_gen = []
pkgdesc = "Data recovery tool for failing block devices"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/ddrescue/ddrescue.html"
source = f"$(GNU_SITE)/ddrescue/ddrescue-{pkgver}.tar.lz"
sha256 = "2264622d309d6c87a1cfc19148292b8859a688e9bc02d4702f5cd4f288745542"
hardening = ["vis", "cfi"]


def init_configure(self):
    # passes only as confargs directly
    self.configure_args += [
        f"CXX={self.get_tool('CXX')}",
        f"CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"LDFLAGS={self.get_ldflags(shell=True)}",
    ]
