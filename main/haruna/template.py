pkgname = "haruna"
pkgver = "1.3.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "extra-cmake-modules",
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "breeze-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "kfilemetadata-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-devel",
    "kwindowsystem-devel",
    "mpvqt-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["kdeclarative", "yt-dlp"]
pkgdesc = "Qt/libmpv based video player"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/haruna"
source = f"$(KDE_SITE)/haruna/{pkgver}/haruna-{pkgver}.tar.xz"
sha256 = "7fe143ff284237ad5e1abf0133f2ac8e86927665b6a3d218405c7e05cd81ba2f"
