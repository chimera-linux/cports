pkgname = "kruler"
pkgver = "26.08.3"
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
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kruler"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kruler-{pkgver}.tar.xz"
sha256 = "fb3f017ab7c10113cbcc29f09948c1040468c6701f765fa46fb24591e0d4ce6b"
