pkgname = "kdegraphics-mobipocket"
pkgver = "25.04.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kio-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE plugins for mobipocket files"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/graphics/kdegraphics-mobipocket"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdegraphics-mobipocket-{pkgver}.tar.xz"
sha256 = "bccfd69e3dbf079a31e06d3ff5ae9db1fc6ef00525163af162e6cc106f0e9079"
hardening = ["vis"]


@subpackage("kdegraphics-mobipocket-devel")
def _(self):
    return self.default_devel()
