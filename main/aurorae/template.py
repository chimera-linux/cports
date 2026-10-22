pkgname = "aurorae"
pkgver = "6.8.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kcmutils-devel",
    "kcolorscheme-devel",
    "kcoreaddons-devel",
    "kdecoration-devel",
    "ki18n-devel",
    "knewstuff-devel",
    "kpackage-devel",
    "ksvg-devel",
    "kwindowsystem-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
# was previously in kwin
replaces = ["kwin<6.4.0"]
pkgdesc = "Themeable window decoration for KWin"
license = "GPL-2.0-or-later"
url = "https://develop.kde.org/docs/plasma/aurorae"
source = f"$(KDE_SITE)/plasma/{pkgver}/aurorae-{pkgver}.tar.xz"
sha256 = "3ffd6381ef5f2ebb4001970ba0ae7a36596ddae7383fa3cc199f9430e72ef281"


@subpackage("aurorae-devel")
def _(self):
    return self.default_devel()
