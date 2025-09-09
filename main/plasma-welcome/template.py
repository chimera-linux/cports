pkgname = "plasma-welcome"
pkgver = "6.4.5"
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
    "kdbusaddons-devel",
    "kdbusaddons-devel",
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
depends = ["kuserfeedback"]
pkgdesc = "KDE onboarding wizard"
license = "GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-welcome"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-welcome-{pkgver}.tar.xz"
sha256 = "57cebb57b5d528263a9d906db258e368dccd84251ae9244ac07be20b59fed609"


def post_install(self):
    self.uninstall("usr/lib/*.a", glob=True)
