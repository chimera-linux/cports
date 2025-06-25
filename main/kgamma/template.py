pkgname = "kgamma"
pkgver = "6.4.1"
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
sha256 = "cc2941c546321c0f40087a81e2c3d8d44ea3845034c164179a6384b54ef0fb90"
hardening = ["vis"]
