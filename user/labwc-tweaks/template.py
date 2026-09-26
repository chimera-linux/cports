pkgname = "labwc-tweaks"
pkgver = "0.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
hostmakedepends = ["cmake", "ninja", "perl", "pkgconf"]
makedepends = ["qt6-qttools-devel"]
depends = ["libxml2", "glib", "qt6-qtbase"]
pkgdesc = "Qt configuration tool for labwc"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://github.com/labwc/labwc-tweaks"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a742250c7e8ea363758a024688226a4296a6798adc57abe0903d580ab195b749"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("BSD-3-Clause")
