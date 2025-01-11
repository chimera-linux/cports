pkgname = "kruler"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kruler"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kruler-{pkgver}.tar.xz"
sha256 = "9a51ebc2208c56102a42151fb4cc67090902ca39bba9a2f74d873807bef7ed1e"
