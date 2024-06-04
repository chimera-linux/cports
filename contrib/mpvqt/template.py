pkgname = "mpvqt"
pkgver = "1.0.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = " LGPL-2.1-only OR LGPL-3.0-only"
url = "https://invent.kde.org/libraries/mpvqt"
source = f"$(KDE_SITE)/mpvqt/mpvqt-{pkgver}.tar.xz"
sha256 = "9131d2a925e5f33e19b9d081dfd5f30d576abd87464d67c70bef41a486f54eb9"
hardening = ["vis", "!cfi"]


@subpackage("mpvqt-devel")
def _devel(self):
    self.depends += [
        "mpv-devel",
        "qt6-qtdeclarative-devel",
    ]
    return self.default_devel()
