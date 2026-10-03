pkgname = "kweather"
pkgver = "26.08.2"
pkgrel = 1
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
    "krunner-devel",
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
sha256 = "b666c8f4f8bc6669512ec244f119bfdb2256338595f2cd2c58095c9a2349bdf1"
