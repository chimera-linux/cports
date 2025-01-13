pkgname = "pulseaudio-qt"
pkgver = "1.7.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/libraries/pulseaudio-qt"
source = f"$(KDE_SITE)/pulseaudio-qt/pulseaudio-qt-{pkgver}.tar.xz"
sha256 = "6a18db76dd2bcc3df7d9a9379c025295817264baa1f2ed8caaac7da44e04e931"
hardening = ["vis"]


@subpackage("pulseaudio-qt-devel")
def _(self):
    return self.default_devel()
