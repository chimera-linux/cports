pkgname = "kcharselect"
pkgver = "25.04.1"
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
    "kbookmarks-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE character picker"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kcharselect"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kcharselect-{pkgver}.tar.xz"
sha256 = "1b4d67e1286f31388fa49f28097bc45d77388c77296db35bc34ace2ad0d9c84a"
