pkgname = "yakuake"
pkgver = "25.08.3"
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
    "karchive-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kparts-devel",
    "kstatusnotifieritem-devel",
    "kwayland-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
depends = ["konsole"]
pkgdesc = "KDE drop-down terminal"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://apps.kde.org/yakuake"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/yakuake-{pkgver}.tar.xz"
sha256 = "d8d3f0ffecfd98f00c8618a7dcf5cf85ef745f704717df8198f6321d83451eec"
