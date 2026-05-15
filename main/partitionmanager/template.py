pkgname = "partitionmanager"
pkgver = "26.04.1"
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
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kjobwidgets-devel",
    "kpmcore-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "polkit-qt-1-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE drive management utility"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/partitionmanager"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/partitionmanager-{pkgver}.tar.xz"
)
sha256 = "4b0f2fd3883f6b8fa5607ed620dc7b422b33b87829c11e6597a869ea2cd5aa74"
