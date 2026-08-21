pkgname = "kcoreaddons"
pkgver = "6.29.0"
pkgrel = 0
build_style = "cmake"
# unpackaged pyside6
configure_args = ["-DBUILD_PYTHON_BINDINGS=OFF"]
# flaky
make_check_args = ["-E", "knetworkmountstestnoconfig"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = [
    "qt6-qtbase-private-devel",  # qlocale_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Qt6 addon library with a collection of non-GUI utilities"
license = "LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcoreaddons-{pkgver}.tar.xz"
sha256 = "771f7fee754a356fa284d0ad7b8b159b890cbbfac082e49ce441b43d4943027e"
hardening = ["vis"]


@subpackage("kcoreaddons-devel")
def _(self):
    return self.default_devel()
