pkgname = "libkleo"
pkgver = "25.08.3"
pkgrel = 0
build_style = "cmake"
# fails on aarch64 at least
# newkeyapprovaldialogtest has wayland die
make_check_args = [
    "-E",
    "(keycachetest|newkeyapprovaldialogtest|keyselectioncombotest)",
]
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
sha256 = "0553b18a295cb5fbff5fae99034a782ae4d07d43d2c1637eaf67a31ca650b816"


@subpackage("libkleo-devel")
def _(self):
    self.depends += ["gpgme-qt-devel"]
    return self.default_devel()
