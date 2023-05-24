pkgname = "tzutils"
pkgver = "2023c"
pkgrel = 0
build_style = "makefile"
make_build_args = ["TZDIR=/usr/share/zoneinfo", "KSHELL=/bin/sh"]
checkdepends = ["groff", "perl", "curl"]
pkgdesc = "Time zone and daylight-saving time utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none AND BSD-3-Clause"
url = "http://www.iana.org/time-zones"
source = f"https://github.com/eggert/tz/archive/{pkgver}.tar.gz"
sha256 = "9aa20ef838183e58f09acca92098cf6aa6d8e229aecf24e098c3af2a38e596f8"
hardening = ["vis", "cfi"]
# needs network access
options = ["!check"]


def do_install(self):
    self.install_bin("zic")
    self.install_bin("zdump")
    self.install_bin("tzselect")
    self.install_man("zic.8")
    self.install_man("zdump.8")
    self.install_man("tzselect.8")
    self.install_license("LICENSE")
