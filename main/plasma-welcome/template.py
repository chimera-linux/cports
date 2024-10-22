pkgname = "plasma-welcome"
pkgver = "6.2.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-welcome"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-welcome-{pkgver}.tar.xz"
sha256 = "0d60f383658b05f82063b603231424e8e93c383d1be1372f019049946e405f91"
