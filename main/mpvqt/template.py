pkgname = "mpvqt"
pkgver = "1.1.1"
pkgrel = 1
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
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/libraries/mpvqt"
source = f"$(KDE_SITE)/mpvqt/mpvqt-{pkgver}.tar.xz"
sha256 = "bdd1ea69338cf3017f628a886218b8c185ca24e8257f03207a3cf1bbb51e3d32"
hardening = ["vis"]


@subpackage("mpvqt-devel")
def _(self):
    self.depends += [
        "mpv-devel",
        "qt6-qtdeclarative-devel",
    ]
    return self.default_devel()
