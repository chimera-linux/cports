pkgname = "aurorae"
pkgver = "6.4.5"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
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
sha256 = "3183eebc476d6763741549c6bd007c650649913d648ccafa303669082d8bf378"


@subpackage("aurorae-devel")
def _(self):
    return self.default_devel()
