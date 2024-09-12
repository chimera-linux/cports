pkgname = "pulseaudio-qt"
pkgver = "1.6.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libpulse-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Pulseaudio Qt bindings"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/libraries/pulseaudio-qt"
source = f"$(KDE_SITE)/pulseaudio-qt/pulseaudio-qt-{pkgver}.tar.xz"
sha256 = "1becbadacb36a9d6a431a0c93cdb428f8f67f37cf2d23768675983318c0ade84"
hardening = ["vis"]


@subpackage("pulseaudio-qt-devel")
def _(self):
    return self.default_devel()
