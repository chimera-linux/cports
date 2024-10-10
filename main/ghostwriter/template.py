pkgname = "ghostwriter"
pkgver = "24.08.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/ghostwriter"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/ghostwriter-{pkgver}.tar.xz"
sha256 = "83e7ff35e7dce03a120adfa998b6030182350b026a9fe6028d0a962918e772e7"
