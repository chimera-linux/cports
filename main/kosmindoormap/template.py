pkgname = "kosmindoormap"
pkgver = "24.12.2"
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
    "qt6-qtbase-private-devel",  # qlocale_tools_p.h
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
sha256 = "8a43b2e157727e44ac4a3ee81ac7049a8a6a425bcb4257b3e824f615cdc2fcee"


@subpackage("kosmindoormap-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
