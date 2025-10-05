pkgname = "kruler"
pkgver = "25.08.1"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libxcb-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
]
pkgdesc = "KDE screen measuring tool"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kruler"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kruler-{pkgver}.tar.xz"
sha256 = "b03638bb846495f9ded02336d1a8b7c1c45b18ea61f5f8299cd2bacb8a382adb"
