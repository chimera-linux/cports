pkgname = "libksane"
pkgver = "24.05.2"
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
sha256 = "6fdcf6d8c38963dc46c60c68ece4f07226fd5d5a0ee1644c908baf797ab54ad9"
# CFI: check
hardening = ["vis", "!cfi"]
# TODO
options = ["!cross"]


@subpackage("libksane-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
