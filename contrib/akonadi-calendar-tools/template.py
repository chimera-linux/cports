pkgname = "akonadi-calendar-tools"
pkgver = "24.08.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/pim/akonadi-calendar-tools"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-calendar-tools-{pkgver}.tar.xz"
sha256 = "44863627bcb44c067feadba935da5b34c23f1b66d750ce98d3b18000f1c233f9"
