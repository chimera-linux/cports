pkgname = "kolourpaint"
pkgver = "24.12.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "extra-cmake-modules", "gettext"]
makedepends = [
    "kcrash-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "libksane-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE paint program"
license = "BSD-2-Clause AND LGPL-2.0-or-later"
url = "https://invent.kde.org/graphics/kolourpaint"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kolourpaint-{pkgver}.tar.xz"
sha256 = "d1097d88df9f7c81325bcbcca6a2e740d3ec877bc9e107aafbeb6c69053f70c1"


def post_install(self):
    self.install_license("COPYING")
