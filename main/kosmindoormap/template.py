pkgname = "kosmindoormap"
pkgver = "25.08.3"
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
    "kirigami-addons-devel",
    "kopeninghours-devel",
    "kpublictransport-devel",
    "kservice-devel",
    "protobuf-devel",
    "qt6-qtbase-private-devel",  # qlocale_tools_p.h
    "qt6-qtdeclarative-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "KDE OSM multi-floor renderer"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/libraries/kosmindoormap"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kosmindoormap-{pkgver}.tar.xz"
)
sha256 = "1a2ce2c3e514bfe01e7b1fde943bf099121cad82a88f444bdac03b57509be3df"


@subpackage("kosmindoormap-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
