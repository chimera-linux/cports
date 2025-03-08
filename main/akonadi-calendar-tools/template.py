pkgname = "akonadi-calendar-tools"
pkgver = "24.12.3"
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
    "akonadi-calendar-devel",
    "akonadi-devel",
    "calendarsupport-devel",
    "kcalendarcore-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "Console utilities for Akonadi calendars"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/pim/akonadi-calendar-tools"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-calendar-tools-{pkgver}.tar.xz"
sha256 = "e5b34b90d6a4c7b6e300d904aa817867eea7ecbfae5c8eec692368d230685703"
