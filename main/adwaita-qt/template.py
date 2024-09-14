pkgname = "adwaita-qt"
pkgver = "1.4.2"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DUSE_QT6=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "qt6-qtbase"]
makedepends = ["qt6-qtbase-devel"]
pkgdesc = "Adwaita style for Qt"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/FedoraQt/adwaita-qt"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "cd5fd71c46271d70c08ad44562e57c34e787d6a8650071db115910999a335ba8"


@subpackage("adwaita-qt-devel")
def _(self):
    return self.default_devel()
