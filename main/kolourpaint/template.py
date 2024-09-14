pkgname = "kolourpaint"
pkgver = "24.08.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "extra-cmake-modules", "gettext"]
makedepends = [
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
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-2-Clause AND LGPL-2.0-or-later"
url = "https://invent.kde.org/graphics/kolourpaint"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kolourpaint-{pkgver}.tar.xz"
sha256 = "30e1192c65f9d16062f9cc78b0936f06f6ebcd347c56e6199fe293d7d4569775"


def post_install(self):
    self.install_license("COPYING")
