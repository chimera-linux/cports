pkgname = "ksanecore"
pkgver = "25.04.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "gperf",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
    "sane-backends-devel",
]
pkgdesc = "KDE integration for SANE"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/libraries-ksanecore"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ksanecore-{pkgver}.tar.xz"
sha256 = "e5a8fdda44d4a27f0c90c2b808e48a737999ec200fd0b70f75fabb33a9013302"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("ksanecore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
