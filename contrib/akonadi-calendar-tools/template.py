pkgname = "akonadi-calendar-tools"
pkgver = "24.05.1"
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
sha256 = "69becb8528060deb9605e5c08b88062b18083342e4f58438ca282a3be1787e80"
