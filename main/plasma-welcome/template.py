pkgname = "plasma-welcome"
pkgver = "6.7.0"
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
    "kcmutils-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdbusaddons-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kjobwidgets-devel",
    "knewstuff-devel",
    "kservice-devel",
    "ksvg-devel",
    "kuserfeedback-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
depends = [
    "kuserfeedback",
    "plasma5support",
]
pkgdesc = "KDE onboarding wizard"
license = "GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-welcome"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-welcome-{pkgver}.tar.xz"
sha256 = "483f16931b6cc2c56668f5420418e7b2f8dad576abaa01bc75546c1361f21903"


def post_install(self):
    self.uninstall("usr/lib/*.a", glob=True)
