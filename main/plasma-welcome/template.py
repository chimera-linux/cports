pkgname = "plasma-welcome"
pkgver = "6.7.91"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "plasma-welcome-self-test"]
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
source = f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/plasma-welcome-{pkgver}.tar.xz"
sha256 = "5429a57fc71aa83b338a9f88973f648c845bbe2cf6e9b0611ec140e7d2905bcd"


def post_install(self):
    self.uninstall("usr/lib/*.a", glob=True)
