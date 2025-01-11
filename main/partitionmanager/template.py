pkgname = "partitionmanager"
pkgver = "24.12.1"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/partitionmanager"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/partitionmanager-{pkgver}.tar.xz"
)
sha256 = "9a8f01da56af7355f2b7215efdeb24e0a379304aa27e7b48039baef8552ca3b0"
