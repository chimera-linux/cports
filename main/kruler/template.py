pkgname = "kruler"
pkgver = "24.12.0"
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
sha256 = "d522d5b7c9648ca84b8f179fe3eea8c9c786a9cc1641da5565b1140dca1c7c5c"
