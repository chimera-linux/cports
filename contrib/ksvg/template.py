pkgname = "ksvg"
pkgver = "6.3.1"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "karchive-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kguiaddons-devel",
    "kirigami-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE Components for handling SVGs"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://invent.kde.org/frameworks/ksvg"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/ksvg-{pkgver}.tar.xz"
)
sha256 = "d85cd66490086998e461bb2caf07e685d65a889681021e3df804f3fa21d3c796"
hardening = ["vis", "!cfi"]


@subpackage("ksvg-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
