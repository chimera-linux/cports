pkgname = "francis"
pkgver = "24.08.2"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kirigami-devel",
    "kirigami-addons-devel",
    "knotifications-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE pomodoro time tracker"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/francis"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/francis-{pkgver}.tar.xz"
sha256 = "6b8cc7f38c24e14c2e797a62299d47099965b38e7205578e3206818c7922ae80"
