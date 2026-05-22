pkgname = "kpmcore"
pkgver = "26.04.1"
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
    "kcoreaddons-devel",
    "ki18n-devel",
    "kwidgetsaddons-devel",
    "polkit-qt-1-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["smartmontools", "util-linux-fdisk"]
pkgdesc = "KDE library for partition management"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/kate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kpmcore-{pkgver}.tar.xz"
sha256 = "d14b349f16bdbbc26086e5eeea71e2fe7d657157fa0721ef3952ea439ee96f9b"
hardening = ["vis"]


@subpackage("kpmcore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
