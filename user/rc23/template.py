pkgname = "rc23"
pkgver = "2.0.4"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Reimplementation of the Plan 9 rc shell"
license = "Zlib"
url = "https://codeberg.org/rc23/rc23"
source = f"https://codeberg.org/rc23/rc23/archive/v{pkgver}.tar.gz"
sha256 = "08d48c6bb287bfe22689e8db6342aa5d7fbb874af6b0625c6cf9f57a55630fbc"

depends = ["readline"]
makedepends = ["readline-devel"]

make_build_args = ["EDIT=readline", "RC_ADDON=1"]


def post_install(self):
    self.install_shell("/usr/bin/rc23")
