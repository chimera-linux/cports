pkgname = "kunitconversion"
pkgver = "6.32.0"
pkgrel = 0
build_style = "cmake"
# unpackaged pyside6
configure_args = ["-DBUILD_PYTHON_BINDINGS=OFF"]
# most tests require network access, pass in cbuild chroot
make_check_args = ["-E", "(category|converter|currencytableinit)test"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = ["ki18n-devel", "qt6-qttools-devel"]
pkgdesc = "KDE Converting physical units"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kunitconversion-{pkgver}.tar.xz"
sha256 = "af5e72a5cf7ee3d036e045441fc84a5e9c142be6d46bd36c1490d1cec5e7ecfd"
hardening = ["vis"]


@subpackage("kunitconversion-devel")
def _(self):
    return self.default_devel()
