pkgname = "kolourpaint"
pkgver = "24.05.2"
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
sha256 = "79b177d7bde8f58035d86e2bf552001127496358a4fa946debd952a1c9f121ba"


def post_install(self):
    self.install_license("COPYING")
