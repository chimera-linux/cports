pkgname = "plasma-pa"
pkgver = "6.1.2"
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
    "kdeclarative-devel",
    "kdbusaddons-devel",
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-pa"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-pa-{pkgver}.tar.xz"
sha256 = "fd84e0336bfdcc13fadee91582fa0a858dc36a155f3e1e5691ddc6ff9c6b4466"
# FIXME: cfi kills systemsettings (when leaving "Sound" page) in libplasma-volume-declarative.so
hardening = ["vis", "!cfi"]
