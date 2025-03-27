pkgname = "ddrescue"
pkgver = "1.29.1"
pkgrel = 0
build_style = "gnu_configure"
# handrolled conf
configure_gen = []
pkgdesc = "Data recovery tool for failing block devices"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/ddrescue/ddrescue.html"
source = f"$(GNU_SITE)/ddrescue/ddrescue-{pkgver}.tar.lz"
sha256 = "ddd7d45df026807835a2ec6ab9c365df2ef19e8de1a50ffe6886cd391e04dd75"
hardening = ["vis", "cfi"]


def init_configure(self):
    # passes only as confargs directly
    self.configure_args += [
        f"CXX={self.get_tool('CXX')}",
        f"CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"LDFLAGS={self.get_ldflags(shell=True)}",
    ]
