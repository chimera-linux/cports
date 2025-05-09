pkgname = "tokodon"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "knotifications-devel",
    "kunifiedpush-devel",
    "purpose-devel",
    "qqc2-desktop-style-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwebsockets-devel",
    "qt6-qtwebview-devel",
    "qtkeychain-devel",
]
depends = [
    "kirigami-addons",
    "kitemmodels",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Mastodon client"
license = "(GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.0-or-later"
url = "https://apps.kde.org/tokodon"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/tokodon-{pkgver}.tar.xz"
sha256 = "37a84b55de80859e9902ae26fefb7486dd1cd6600f5bcc3cb3ec9ce6c869f7e3"
