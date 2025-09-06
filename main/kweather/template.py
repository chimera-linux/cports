pkgname = "kweather"
pkgver = "25.08.0"
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
sha256 = "acd8d383abc97323a08283f5c34511d05a06b7019320d024968a01ccf6fe2106"
