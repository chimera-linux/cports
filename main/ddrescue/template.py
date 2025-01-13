pkgname = "ddrescue"
pkgver = "1.29"
pkgrel = 0
build_style = "gnu_configure"
# handrolled conf
configure_gen = []
pkgdesc = "Data recovery tool for failing block devices"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/ddrescue/ddrescue.html"
source = f"$(GNU_SITE)/ddrescue/ddrescue-{pkgver}.tar.lz"
sha256 = "01a414327853b39fba2fd0ece30f7bee2e9d8c8e8eb314318524adf5a60039a3"
hardening = ["vis", "cfi"]


def init_configure(self):
    # passes only as confargs directly
    self.configure_args += [
        f"CXX={self.get_tool('CXX')}",
        f"CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"LDFLAGS={self.get_ldflags(shell=True)}",
    ]
