pkgname = "spc2it"
pkgver = "0.4.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "ninja"]
pkgdesc = "Utility for converting SPC700 music files to Impulse Tracker modules"
maintainer = "theuae <theuae@nanachi.network>"
license = "GPL-2.0-or-later"
url = "https://github.com/uyjulian/spc2it"
source = f"https://github.com/uyjulian/spc2it/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5f30b0d88a8120ad30cc3a0052441c3d605ee9f165d863bcbeef7c915562a9fa"
def post_install(self):
    self.install_license("doc/LICENSE_SNEESE")
    self.install_bin("build/spc2it")


    

