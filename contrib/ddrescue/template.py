pkgname = "ddrescue"
pkgver = "1.28"
pkgrel = 0
build_style = "gnu_configure"
# handrolled conf
configure_gen = []
pkgdesc = "Data recovery tool for failing block devices"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/ddrescue/ddrescue.html"
source = f"$(GNU_SITE)/ddrescue/ddrescue-{pkgver}.tar.lz"
sha256 = "6626c07a7ca1cc1d03cad0958522c5279b156222d32c342e81117cfefaeb10c1"
hardening = ["vis", "cfi"]


def init_configure(self):
    # passes only as confargs directly
    self.configure_args += [
        f"CXX={self.get_tool('CXX')}",
        f"CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"LDFLAGS={self.get_ldflags(shell=True)}",
    ]
