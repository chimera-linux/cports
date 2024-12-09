pkgname = "log4cplus"
pkgver = "2.1.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Logging library for C++"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "Apache-2.0 AND BSD-2-Clause"
url = "https://log4cplus.github.io/log4cplus"
source = f"https://downloads.sourceforge.net/sourceforge/log4cplus/log4cplus-stable/log4cplus-{pkgver}.tar.xz"
sha256 = "fbdabb4ef734fe1cc62169b23f0b480cc39127ac7b09b810a9c1229490d67e9e"


def post_install(self):
    self.install_license("LICENSE")
