pkgname = "pulseaudio-qt"
pkgver = "1.5.0"
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
sha256 = "cd8f51c8700073d0fd90d5784083aceb73e72ba9a704e605e0a67909426a8520"
hardening = ["vis", "!cfi"]


@subpackage("pulseaudio-qt-devel")
def _devel(self):
    return self.default_devel()
