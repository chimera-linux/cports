pkgname = "ghostwriter"
pkgver = "25.12.1"
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
sha256 = "dc8b24cd488dbbc7ed3c2d7ecc37ab475e69ac0d65c4cfdd833a29f41799792c"
