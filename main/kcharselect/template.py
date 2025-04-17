pkgname = "kcharselect"
pkgver = "25.04.0"
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
sha256 = "4de53cd099291e046cf479878688cd2689a7e7f9ee27550d9b03703323cab4a4"
