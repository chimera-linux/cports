pkgname = "plasma-systemmonitor"
pkgver = "6.5.5"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
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
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://apps.kde.org/plasma-systemmonitor"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-systemmonitor-{pkgver}.tar.xz"
sha256 = "8be93fa95d510f2b53ac8a86f7e66aa10e5480af3632e419689bdb5ad33ef1fe"
hardening = ["vis"]
