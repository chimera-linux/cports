pkgname = "kcharselect"
pkgver = "26.04.1"
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
sha256 = "9a8af0148b9f1686f6a3c9746f553ecd8107e386acacaed34018b25269cdec1d"
