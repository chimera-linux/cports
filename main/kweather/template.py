pkgname = "kweather"
pkgver = "26.04.3"
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
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "ki18n-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kweathercore-devel",
    "libplasma-devel",
    "qt6-qtcharts-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE Weather application"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kweather"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kweather-{pkgver}.tar.xz"
sha256 = "3d22d401742715333c2566fdb3902f82d561ee1e75f677fe958e9f161cf9021a"
