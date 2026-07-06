pkgname = "khelpcenter"
pkgver = "26.04.3"
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
sha256 = "b1101a10cee699cc2cfcebdda2c7fd0d0b444998a50886845ae057acddca6c79"
