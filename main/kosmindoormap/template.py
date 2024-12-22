pkgname = "kosmindoormap"
pkgver = "24.12.0"
pkgrel = 1
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
sha256 = "f2a648d8dab8e568448fddcddd2bcc76387b6231cd6aca355030491aa6a336c1"


@subpackage("kosmindoormap-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
