pkgname = "khelpcenter"
pkgver = "25.08.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "kbookmarks-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kservice-devel",
    "ktexttemplate-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwebengine-devel",
    "xapian-core-devel",
]
checkdepends = ["perl"]
pkgdesc = "KDE application documentation viewer"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/khelpcenter"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/khelpcenter-{pkgver}.tar.xz"
sha256 = "d84ab8c1d932489421461d6cd5560b295584135b16898150466053353011069a"
