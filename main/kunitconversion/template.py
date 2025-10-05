pkgname = "kunitconversion"
pkgver = "6.18.0"
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
url = "https://api.kde.org/frameworks/kunitconversion/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kunitconversion-{pkgver}.tar.xz"
sha256 = "23a4a5d994666f9db2a5a3c251038f2ef1d978411950925702fb79060ced31c8"
hardening = ["vis"]


@subpackage("kunitconversion-devel")
def _(self):
    return self.default_devel()
