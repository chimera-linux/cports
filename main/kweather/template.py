pkgname = "kweather"
pkgver = "26.08.0"
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
sha256 = "812726baf1e8df7d11176ab51c3fe1e1c895e4560ed6942df0c645bbbb8dcd0c"
