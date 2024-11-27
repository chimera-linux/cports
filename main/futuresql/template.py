pkgname = "futuresql"
pkgver = "0.1.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qcoro-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Non-blocking database framework for Qt"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://api.kde.org/futuresql/html"
source = f"$(KDE_SITE)/futuresql/futuresql-{pkgver}.tar.xz"
sha256 = "e44ed8d5a9618b3ca7ba2983ed9c5f7572e6e0a5b199f94868834b71ccbebd43"


@subpackage("futuresql-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
