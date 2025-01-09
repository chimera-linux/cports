pkgname = "ksvg"
pkgver = "6.9.0"
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
sha256 = "ccd736e032a4089e1d1b2f829b55407ffd333a183f8cca1ad41184e68b9ebcd6"
hardening = ["vis"]


@subpackage("ksvg-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
