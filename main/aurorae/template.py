pkgname = "aurorae"
pkgver = "6.5.1"
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
sha256 = "9c30ef238895435f55f7744d1e5418c10a8eef1b79d9734142627e55978a1bec"


@subpackage("aurorae-devel")
def _(self):
    return self.default_devel()
