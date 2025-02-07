pkgname = "libksane"
pkgver = "24.12.2"
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
    "ksanecore-devel",
    "ktextwidgets-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE image scanning library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/graphics/libksane"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libksane-{pkgver}.tar.xz"
sha256 = "cc38a3d399525f8a9f2b62271e460794a6376a858c2140bab73bb0405f85a062"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("libksane-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
