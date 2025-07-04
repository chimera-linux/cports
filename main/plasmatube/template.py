pkgname = "plasmatube"
pkgver = "25.04.3"
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
sha256 = "bd05e3b4ca3be87d05c232df92683bfbd58bb6239d18ad601abe4b4e9cf9b0fb"
