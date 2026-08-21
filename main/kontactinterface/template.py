pkgname = "kontactinterface"
pkgver = "26.08.0"
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
sha256 = "70e37fb8fd13a89e8f34ed34b69d8d7720d6e169d21f982dce4d77d8856951cd"


@subpackage("kontactinterface-devel")
def _(self):
    self.depends += ["kparts-devel"]
    return self.default_devel()
