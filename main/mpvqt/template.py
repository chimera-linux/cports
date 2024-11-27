pkgname = "mpvqt"
pkgver = "1.0.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "mpv-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "QML libmpv wrapper"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = " LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/libraries/mpvqt"
source = f"$(KDE_SITE)/mpvqt/mpvqt-{pkgver}.tar.xz"
sha256 = "9f37b85f319c27f6244743c4259402b0aa2474ed851f0d833d9bd2a0731c178c"
hardening = ["vis"]


@subpackage("mpvqt-devel")
def _(self):
    self.depends += [
        "mpv-devel",
        "qt6-qtdeclarative-devel",
    ]
    return self.default_devel()
