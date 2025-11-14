pkgname = "kgamma"
pkgver = "6.5.2"
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
    "kcmutils-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE tool for adjusting monitor gamma"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/kgamma"
source = f"$(KDE_SITE)/plasma/{pkgver}/kgamma-{pkgver}.tar.xz"
sha256 = "538353ffcdfb7e6d66e16b1a3fafffa478b293c7d57656ca71016f2aeb782eee"
hardening = ["vis"]
