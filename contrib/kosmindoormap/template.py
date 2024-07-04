pkgname = "kosmindoormap"
pkgver = "24.05.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "bison",
    "cmake",
    "extra-cmake-modules",
    "flex",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "ki18n-devel",
    "kopeninghours-devel",
    "kpublictransport-devel",
    "kservice-devel",
    "protobuf-devel",
    "qt6-qtdeclarative-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "KDE OSM multi-floor renderer"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/libraries/kosmindoormap"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kosmindoormap-{pkgver}.tar.xz"
)
sha256 = "956e7df11e28957866c9ee4de0d08b6a59ecf769862799e95cd424683782ccc6"


@subpackage("kosmindoormap-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
