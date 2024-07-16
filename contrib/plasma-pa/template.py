pkgname = "plasma-pa"
pkgver = "6.1.3"
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
sha256 = "4211b05f036d80e455a4c2a32184266017fe5dcd01fb7532760ac81d886aadf7"
# CFI: kills systemsettings (when leaving "Sound" page) in libplasma-volume-declarative.so
hardening = ["vis", "!cfi"]
