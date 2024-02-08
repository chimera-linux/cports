pkgname = "log4cplus"
pkgver = "2.1.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Logging library for C++"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "Apache-2.0 AND BSD-2-Clause"
url = "https://log4cplus.github.io/log4cplus"
source = f"https://downloads.sourceforge.net/sourceforge/{pkgname}/{pkgname}-stable/{pkgname}-{pkgver}.tar.xz"
sha256 = "a1d8e67a207f90a9dd4f82b28a1f3ac6dead5a80c2bed071277a9e865698a82b"


def post_install(self):
    self.install_license("LICENSE")
