pkgname = "libksane"
pkgver = "26.04.1"
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
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/graphics/libksane"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libksane-{pkgver}.tar.xz"
sha256 = "8d78335f78f35872afab3b206244235518b754dd2a2fcd528e716ea0df1fee1d"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("libksane-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
