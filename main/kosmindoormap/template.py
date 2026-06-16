pkgname = "kosmindoormap"
pkgver = "26.04.2"
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
sha256 = "418143d92129b44213be6fe4846a75bab94cfbeb9ba6367667b2a2057d17f2e6"


@subpackage("kosmindoormap-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
