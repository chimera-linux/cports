pkgname = "kontactinterface"
pkgver = "26.08.1"
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
    "kcoreaddons-devel",
    "ki18n-devel",
    "kparts-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Kontact plugin interface library"
license = "LGPL-3.0-only"
url = "https://community.kde.org/KDE_PIM"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kontactinterface-{pkgver}.tar.xz"
)
sha256 = "c330d3c6f531ec13cd0dd2f291ca12a787cbc35cc4c9a1722e4d117d456eb821"


@subpackage("kontactinterface-devel")
def _(self):
    self.depends += ["kparts-devel"]
    return self.default_devel()
