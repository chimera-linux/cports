pkgname = "tzutils"
pkgver = "2021d"
pkgrel = 0
build_style = "makefile"
make_build_args = ["TZDIR=/usr/share/zoneinfo", "KSHELL=/bin/sh"]
checkdepends = ["groff", "perl"]
pkgdesc = "Time zone and daylight-saving time utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none AND BSD-3-Clause"
url = "http://www.iana.org/time-zones"
source = f"https://github.com/eggert/tz/archive/{pkgver}.tar.gz"
sha256 = "2e6b14cfe3ee389f67887c36436cc40ff11266e5c2213295c1528f42a65dc98e"
# missing checkdepends
options = ["!check"]

def do_install(self):
    self.install_bin("zic")
    self.install_bin("zdump")
    self.install_bin("tzselect")
    self.install_man("zic.8")
    self.install_man("zdump.8")
    self.install_man("tzselect.8")
    self.install_license("LICENSE")
