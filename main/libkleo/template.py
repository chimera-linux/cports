pkgname = "libkleo"
pkgver = "25.04.0"
pkgrel = 1
build_style = "cmake"
# fails on aarch64 at least
make_check_args = ["-E", "keycachetest"]
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
sha256 = "7ce247b7a3f5788ac524841b8c8a32c53b4ee49093310b91d29dc5d8010cafd8"


@subpackage("libkleo-devel")
def _(self):
    self.depends += ["gpgme-qt-devel"]
    return self.default_devel()
