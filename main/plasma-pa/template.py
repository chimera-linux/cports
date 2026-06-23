pkgname = "plasma-pa"
pkgver = "6.7.1"
pkgrel = 0
build_style = "cmake"
# FIXME: only test, needs selenium-webdriver-at-spi-run
make_check_args = ["-E", "applettest"]
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
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kdeclarative-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kstatusnotifieritem-devel",
    "ksvg-devel",
    "kwindowsystem-devel",
    "libcanberra-devel",
    "libplasma-devel",
    "libpulse-devel",
    "pulseaudio-qt-devel",
    "qt6-qtdeclarative-devel",
]
depends = [
    "kirigami-addons",
    "kitemmodels",
]
pkgdesc = "KDE Plasma PulseAudio integration"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-pa"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-pa-{pkgver}.tar.xz"
sha256 = "70e9e47527f38b9159f941dc8895a849828b3f6e313e33b39e11db43203f1709"
hardening = ["vis"]
