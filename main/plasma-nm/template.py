pkgname = "plasma-nm"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "(kcm_.*_smoketest|mobileproviderstest)"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kcolorscheme-devel",
    "kcompletion-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "knotifications-devel",
    "ksvg-devel",
    "kwallet-devel",
    "libplasma-devel",
    "modemmanager-qt-devel",
    "networkmanager-qt-devel",
    "prison-devel",
    "qca-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
    # TODO: openconnect>=3.99 -> qt6-qtwebengine-devel
]
depends = ["prison"]
pkgdesc = "KDE Plasma NetworkManager integration"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-nm"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-nm-{pkgver}.tar.xz"
sha256 = "b29680cc17c4bbe52e3b988d5be437ec4b524b554fa180ead13bc8910144cf98"
hardening = ["vis"]
