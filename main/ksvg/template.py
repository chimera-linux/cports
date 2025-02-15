pkgname = "ksvg"
pkgver = "6.11.0"
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
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ksvg-{pkgver}.tar.xz"
)
sha256 = "053092e36b76deeffe19629ae12a372b172f947bee3cc2034c68e7ba4e1da6cf"
hardening = ["vis"]


@subpackage("ksvg-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
