pkgname = "plasma-welcome"
pkgver = "6.3.4"
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
    "kirigami-devel",
    "kirigami-addons-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kconfigwidgets-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "knewstuff-devel",
    "kservice-devel",
    "kwindowsystem-devel",
    "kdbusaddons-devel",
    "kcmutils-devel",
    "ksvg-devel",
    "kjobwidgets-devel",
    "kuserfeedback-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
depends = ["kuserfeedback"]
pkgdesc = "KDE onboarding wizard"
license = "GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-welcome"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-welcome-{pkgver}.tar.xz"
sha256 = "33d552e398f2145f9519056f989de0066cc8fdca6961a309d7a0ace6dcef39b3"
