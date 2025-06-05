pkgname = "tokodon"
pkgver = "25.04.2"
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
sha256 = "399ed21708a67a4fc3f5fdffb1630af1be6a82d526b9b64d53e956eec7954bac"
