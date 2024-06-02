pkgname = "libksane"
pkgver = "24.05.0"
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
sha256 = "e73c6f1a65ae40daecd994c29aae0e879b9832f00783ea229a5c8970691711c8"
# CFI: check
hardening = ["vis", "!cfi"]
# TODO
options = ["!cross"]


@subpackage("libksane-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
