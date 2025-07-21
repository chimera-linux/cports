pkgname = "haruna"
pkgver = "1.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
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
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/haruna"
source = f"$(KDE_SITE)/haruna/{pkgver}/haruna-{pkgver}.tar.xz"
sha256 = "3cb47be3148dcc8637ff5262573390ca5edc2ece00028af790d7355347d8df6e"
