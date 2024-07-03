pkgname = "plasma-systemmonitor"
pkgver = "6.1.2"
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
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "knewstuff-devel",
    "kpackage-devel",
    "kservice-devel",
    "libksysguard-devel",
    "qt6-qtdeclarative-devel",
]
depends = [
    "kquickcharts",
    "ksystemstats",
]
pkgdesc = "KDE System Resource Usage Monitor"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://apps.kde.org/plasma-systemmonitor"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-systemmonitor-{pkgver}.tar.xz"
sha256 = "ba87d6f7f4c3c9edfcb37574d12379849521a2286bcd16d75c584a901d4c62ec"
# FIXME: cfi crash on launch
hardening = ["vis", "!cfi"]
