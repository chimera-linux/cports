pkgname = "ghostwriter"
pkgver = "26.08.1"
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
sha256 = "59f0ca6d31e881d7e5aaa76f386ae2d42b3e4da9cf959224526b3d12addd4ef6"
