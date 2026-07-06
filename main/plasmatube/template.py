pkgname = "plasmatube"
pkgver = "26.04.3"
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
sha256 = "91a997e40f7c21da2ed081050cdde8b007626627b8d1d74c20ad6b8a17e1a597"
