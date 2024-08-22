pkgname = "libkleo"
pkgver = "24.08.0"
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
    "boost-devel",
    "gpgme-qt-devel",
    "kcodecs-devel",
    "kcolorscheme-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kitemmodels-devel",
    "ktextaddons-devel",
    "kwidgetsaddons-devel",
    "libgpg-error-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM cryptography library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://invent.kde.org/pim/libkleo"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkleo-{pkgver}.tar.xz"
sha256 = "951657eb625686f13305fdae1d52e0c5e5a108e1f3ba03d1080239a0c0f531f1"


@subpackage("libkleo-devel")
def _(self):
    self.depends += ["gpgme-qt-devel"]
    return self.default_devel()
