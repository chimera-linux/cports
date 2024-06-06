pkgname = "haruna"
pkgver = "1.1.2"
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
depends = ["yt-dlp"]
pkgdesc = "Qt/libmpv based video player"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/haruna"
source = f"$(KDE_SITE)/haruna/{pkgver}/haruna-{pkgver}.tar.xz"
sha256 = "cb01323f1195a3d8994121e66492c29d27c021fb2a5784b78ce5c06c0bb88683"
