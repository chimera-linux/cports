pkgname = "kde-cli-tools"
pkgver = "6.1.3"
pkgrel = 0
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
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "KDE command line tools to interact with Plasma"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kde-cli-tools"
source = f"$(KDE_SITE)/plasma/{pkgver}/kde-cli-tools-{pkgver}.tar.xz"
sha256 = "d969051e2832ca6eb00ebc22234834e46a2f3cbfc6c3d4ee8a962058b14bc87a"
hardening = ["vis"]
