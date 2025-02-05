pkgname = "lm-sensors"
pkgver = "3.6.0"
pkgrel = 2
build_style = "makefile"
make_build_args = [f"MACHINE={self.profile().arch}"]
make_install_args = ["SBINDIR=/usr/bin", "MANDIR=/usr/share/man"]
hostmakedepends = ["flex", "bison", "perl"]
depends = ["perl"]
pkgdesc = "Sensor reading utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/lm-sensors/lm-sensors"
source = f"{url}/archive/V{pkgver.replace('.', '-')}.tar.gz"
sha256 = "0591f9fa0339f0d15e75326d0365871c2d4e2ed8aa1ff759b3a55d3734b7d197"
# no test suite
options = ["!check"]

# TODO: service for fancontrol


@subpackage("lm-sensors-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libsensors")]

    return self.default_libs()


@subpackage("lm-sensors-devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libsensors-devel")]

    return self.default_devel()
