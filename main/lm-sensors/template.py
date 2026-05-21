pkgname = "lm-sensors"
pkgver = "3.6.2"
pkgrel = 0
build_style = "makefile"
make_build_args = [f"MACHINE={self.profile().arch}"]
make_install_args = ["SBINDIR=/usr/bin", "MANDIR=/usr/share/man"]
hostmakedepends = ["flex", "bison", "perl"]
depends = ["perl"]
pkgdesc = "Sensor reading utilities"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/lm-sensors/lm-sensors"
source = f"{url}/archive/V{pkgver.replace('.', '-')}.tar.gz"
sha256 = "c6a0587e565778a40d88891928bf8943f27d353f382d5b745a997d635978a8f0"
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
