pkgname = "kolourpaint"
pkgver = "25.08.0"
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
sha256 = "6c89b27490f8d8e6cf69114d056f9d96bb7bd7a8177086c74055fa875c123df6"


def post_install(self):
    self.install_license("COPYING")
