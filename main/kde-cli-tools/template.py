pkgname = "kde-cli-tools"
pkgver = "6.2.4"
pkgrel = 1
build_style = "cmake"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kde-cli-tools"
source = f"$(KDE_SITE)/plasma/{pkgver}/kde-cli-tools-{pkgver}.tar.xz"
sha256 = "117acba7d68006e0299fd68128b6fe54859e920e0e38a4f394998ab88111d9e7"
hardening = ["vis"]
