pkgname = "kde-cli-tools"
pkgver = "6.5.5"
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
sha256 = "083b5d3c8e6315554547e1fc538c7d9f0671e08f7c52f2bc0a5a345027a12279"
hardening = ["vis"]
