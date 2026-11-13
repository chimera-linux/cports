pkgname = "kontactinterface"
pkgver = "26.08.3"
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
sha256 = "035f6d8dec6b578d7b0f9ab7f6dbee05163fb39606b37bb1c410157f03eb2fe5"


@subpackage("kontactinterface-devel")
def _(self):
    self.depends += ["kparts-devel"]
    return self.default_devel()
