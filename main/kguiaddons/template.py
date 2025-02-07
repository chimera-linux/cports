pkgname = "kguiaddons"
pkgver = "6.10.0"
pkgrel = 1
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "plasma-wayland-protocols",
    "qt6-qtbase-private-devel",  # qtguiglobal_p.h
    "qt6-qtwayland-devel",
]
pkgdesc = "KDE addons to QtGui"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://api.kde.org/frameworks/kguiaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kguiaddons-{pkgver}.tar.xz"
sha256 = "b3be04077313e559c5a8f66491d5d286cefe947aaf7c8937544ce85af4853ffa"
hardening = ["vis"]


@subpackage("kguiaddons-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
