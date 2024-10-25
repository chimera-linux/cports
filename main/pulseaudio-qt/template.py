pkgname = "pulseaudio-qt"
pkgver = "1.6.1"
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
sha256 = "f21bf30f2ff3e670d2046f966069dc23f5e653ff56bacdb8920c1374264cbc1e"
hardening = ["vis"]


@subpackage("pulseaudio-qt-devel")
def _(self):
    return self.default_devel()
