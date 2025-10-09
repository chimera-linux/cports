pkgname = "juk"
pkgver = "25.08.2"
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
    "kcompletion-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kjobwidgets-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "ktextwidgets-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "phonon-devel",
    "qt6-qtbase-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "taglib-devel",
]
# TODO: can't play anything without a phonon backend (vlc)
pkgdesc = "KDE music player and manager"
license = "GPL-2.0-only"
url = "https://juk.kde.org"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/juk-{pkgver}.tar.xz"
sha256 = "2b396a80378ae72813d02986b6a3502c975065b49a9feaf382426c7a965a48a0"
