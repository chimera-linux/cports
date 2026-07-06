pkgname = "ksanecore"
pkgver = "26.04.3"
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
sha256 = "e5c96840ba21e7afa6e0635b21cc117552898b14628d9555f2a600c77884747d"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("ksanecore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
