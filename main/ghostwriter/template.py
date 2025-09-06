pkgname = "ghostwriter"
pkgver = "25.08.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "hunspell-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "qt6-qt5compat-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwebengine-devel",
    "sonnet-devel",
]
depends = ["cmark"]
pkgdesc = "KDE markdown editor"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/ghostwriter"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ghostwriter-{pkgver}.tar.xz"
sha256 = "e263840e6e4a5f24ca46c615cfafd0c4b792349bb66354a40ac3beef00b5d8b7"
