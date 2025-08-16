pkgname = "libksieve"
pkgver = "25.08.0"
pkgrel = 0
build_style = "cmake"
# sieveeditorhelphtmlwidgettest: qtwebengine doesnt work in chroot
# findbar-findbarbasetest: failed focus tracking
make_check_args = [
    "-E",
    "(sieveeditorhelphtmlwidgettest|findbar-findbarbasetest)",
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
    "karchive-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kmailtransport-devel",
    "kmime-devel",
    "knewstuff-devel",
    "ktextaddons-devel",
    "libkdepim-devel",
    "libsasl-devel",
    "pimcommon-devel",
    "qt6-qtbase-devel",
    "qt6-qtwebengine-devel",
    "sonnet-devel",
    "syntax-highlighting-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Sieve scripting library"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://api.kde.org/kdepim/libksieve/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libksieve-{pkgver}.tar.xz"
sha256 = "a7e6e6f52377dc07750bdcef835d9fcc63088577b30fdff07ff710600cb1fe76"


@subpackage("libksieve-devel")
def _(self):
    self.depends += ["syntax-highlighting-devel"]
    return self.default_devel()
