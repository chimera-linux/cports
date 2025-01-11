pkgname = "kpublictransport"
pkgver = "24.12.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "networkmanager-qt-devel",
    "protobuf-devel",
    "qt6-qtdeclarative-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "KDE library for accessing public transport information"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kpublictransport/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kpublictransport-{pkgver}.tar.xz"
)
sha256 = "6aa1a526e01abaad0ed8af5484219496eae0bbe8b87e76e65dea05d47d4221c2"


@subpackage("kpublictransport-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel", "zlib-ng-compat-devel"]
    return self.default_devel()
