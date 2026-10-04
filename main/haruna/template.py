pkgname = "haruna"
pkgver = "1.8.1"
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
    "kdsingleapplication-devel",
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
depends = ["kdeclarative", "kitemmodels", "yt-dlp"]
pkgdesc = "Qt/libmpv based video player"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/haruna"
source = f"$(KDE_SITE)/haruna/{pkgver}/haruna-{pkgver}.tar.xz"
sha256 = "01f154e3161292da606899c3017f863362e00bb2402a2796be5e8d6849fc4b4b"
