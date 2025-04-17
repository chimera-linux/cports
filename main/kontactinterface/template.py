pkgname = "kontactinterface"
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
url = "https://api.kde.org/kdepim/kontactinterface/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kontactinterface-{pkgver}.tar.xz"
)
sha256 = "ffcdf272b77ba9ef73dc829504c60d9980113aed9bc8830256c8dec10e351c54"


@subpackage("kontactinterface-devel")
def _(self):
    self.depends += ["kparts-devel"]
    return self.default_devel()
