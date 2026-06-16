pkgname = "kcharselect"
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
sha256 = "4e4e1037da17e3374a83615089cb9a51935675a2eb2409ff22ad98f7578fdd6e"
