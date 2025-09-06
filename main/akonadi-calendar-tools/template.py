pkgname = "akonadi-calendar-tools"
pkgver = "25.08.0"
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
sha256 = "27e6d5aca728bbdc156382f2e783b5ed2f8c443dc5e3bfc3bd2d89391c166de8"
