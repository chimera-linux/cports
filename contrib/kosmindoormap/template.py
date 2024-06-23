pkgname = "kosmindoormap"
pkgver = "24.05.1"
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
    "zlib-devel",
]
pkgdesc = "KDE OSM multi-floor renderer"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/libraries/kosmindoormap"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kosmindoormap-{pkgver}.tar.xz"
)
sha256 = "91e5f12eb2e2f899a118e1b0b53fda55a076566c8504fa80ce6f35b8703dd837"


@subpackage("kosmindoormap-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
