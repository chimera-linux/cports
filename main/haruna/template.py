pkgname = "haruna"
pkgver = "1.3.3"
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
sha256 = "d7fd662c8d3b795deb26fe0e6214731cd7b82cd1983b2b4fc0506e435c0ccc79"
