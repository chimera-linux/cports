pkgname = "ssss"
pkgver = "0.5.7"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["xmltoman"]
makedepends = ["gmp-devel"]
pkgdesc = "Shamir's Secret Sharing Scheme"
license = "GPL-2.0-only"
url = "https://github.com/MrJoy/ssss"
source = f"{url}/archive/refs/tags/releases/v{pkgver}.tar.gz"
sha256 = "dbb1f03797cb3fa69594530f9b2c36010f66705b9d5fbbc27293dce72b9c9473"
# Has no tests
options = ["!check"]


def install(self):
    self.install_bin("ssss-split")
    self.install_link("usr/bin/ssss-combine", "ssss-split")
    self.install_man("ssss*.1", glob=True)
