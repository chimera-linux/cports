pkgname = "plasma-welcome"
pkgver = "6.8.3"
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
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-welcome-{pkgver}.tar.xz"
sha256 = "daa328c588f216ee50db8b1e7fec0d6239c4b06b6b69d4e6225c8677e785a4e8"


def post_install(self):
    self.uninstall("usr/lib/*.a", glob=True)
