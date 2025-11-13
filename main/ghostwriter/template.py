pkgname = "ghostwriter"
pkgver = "25.08.3"
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
sha256 = "399969ef0707cf4883fce172d6a22dfaf29294a9b0fad2e716ad68045202b006"
