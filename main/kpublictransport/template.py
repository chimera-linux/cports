pkgname = "kpublictransport"
pkgver = "24.12.0"
pkgrel = 1
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
sha256 = "b1e0f9498219e5733d47d2c8b60082201ea285215e392831a587267e2c683250"


@subpackage("kpublictransport-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel", "zlib-ng-compat-devel"]
    return self.default_devel()
