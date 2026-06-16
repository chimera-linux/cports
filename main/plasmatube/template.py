pkgname = "plasmatube"
pkgver = "26.04.2"
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
    "kdbusaddons-devel",
    "ki18n-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kwindowsystem-devel",
    "mpvqt-devel",
    "purpose-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qtkeychain-devel",
]
depends = [
    "kdeclarative",
    "kirigami-addons",
    "kitemmodels",
    "purpose",
    "yt-dlp",
]
pkgdesc = "KDE Youtube player"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/plasmatube"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/plasmatube-{pkgver}.tar.xz"
sha256 = "44b261c2b858b981c0f63cab0aa8da3cf4f2f3bc9ec5d8bc513224e6d2332de0"
