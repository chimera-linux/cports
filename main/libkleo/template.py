pkgname = "libkleo"
pkgver = "25.08.0"
pkgrel = 1
build_style = "cmake"
# fails on aarch64 at least
# newkeyapprovaldialogtest has wayland die
make_check_args = ["-E", "(keycachetest|newkeyapprovaldialogtest)"]
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
license = "GPL-3.0-or-later"
url = "https://invent.kde.org/pim/libkleo"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkleo-{pkgver}.tar.xz"
sha256 = "20c9553c7652f8bc59949cf4b92711c7b0e5a486fc4b10d851346439056d2bd4"


@subpackage("libkleo-devel")
def _(self):
    self.depends += ["gpgme-qt-devel"]
    return self.default_devel()
