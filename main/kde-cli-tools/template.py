pkgname = "kde-cli-tools"
pkgver = "6.5.1"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
# FIXME: only test fails on initTestCase() 'fakeApplicationService' returned FALSE
make_check_args = ["-E", "filetypestest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kconfig-devel",
    "kdesu-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kparts-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE command line tools to interact with Plasma"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kde-cli-tools"
source = f"$(KDE_SITE)/plasma/{pkgver}/kde-cli-tools-{pkgver}.tar.xz"
sha256 = "74661d8dc71a345b90651775980b0ad3afb288194af06aa33abc698e0183e2c3"
hardening = ["vis"]
