pkgname = "plasmatube"
pkgver = "24.12.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/plasmatube"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/plasmatube-{pkgver}.tar.xz"
sha256 = "4d72dbe0255a274cf6809dd34e8c6c3e3e78d1f0fff0190483c97d0606675554"
