pkgname = "kquickimageeditor"
pkgver = "0.7.0.1"
pkgrel = 0
build_style = "cmake"
# some hwy nonsense
make_check_args = ["-E", "stackblur.*"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "highway-devel",
    "kconfig-devel",
    "libplasma-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "QML image editing components"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/libraries/kquickimageeditor"
source = f"$(KDE_SITE)/kquickimageeditor/kquickimageeditor-{pkgver}.tar.xz"
sha256 = "b65f32c44bd126cea5e1b5a6eb7cb0eb517277cb8de06675fa6be624b7da381a"


@subpackage("kquickimageeditor-devel")
def _(self):
    return self.default_devel()
