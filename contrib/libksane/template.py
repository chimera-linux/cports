pkgname = "libksane"
pkgver = "24.08.0"
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
sha256 = "4bfbc56289b18fc020809d5cb89185094783370728e02b7cdd2a3832b609bb3d"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("libksane-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
