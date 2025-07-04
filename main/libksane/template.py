pkgname = "libksane"
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
sha256 = "eab97e319cd8e020e63c49ca3c18188898d326d3568c939a5640b42cdc1c265f"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("libksane-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
