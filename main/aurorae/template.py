pkgname = "aurorae"
pkgver = "6.4.0"
pkgrel = 1
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kcolorscheme-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kcmutils-devel",
    "knewstuff-devel",
    "kpackage-devel",
    "ksvg-devel",
    "kwindowsystem-devel",
    "kdecoration-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
# was previously in kwin
replaces = ["kwin<6.4.0"]
pkgdesc = "Themeable window decoration for KWin"
license = "GPL-2.0-or-later"
url = "https://develop.kde.org/docs/plasma/aurorae"
source = f"$(KDE_SITE)/plasma/{pkgver}/aurorae-{pkgver}.tar.xz"
sha256 = "563c4285f426848256e92c884a058a572d59df5ab9a4c8b907385226ec4ac0b2"


@subpackage("aurorae-devel")
def _(self):
    return self.default_devel()
