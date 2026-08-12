pkgname = "plasma-welcome"
pkgver = "6.7.4"
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
sha256 = "d9862440a16820ca00abb22363be57e9b156adc76db692d4d04cabd3e862ab3d"


def post_install(self):
    self.uninstall("usr/lib/*.a", glob=True)
