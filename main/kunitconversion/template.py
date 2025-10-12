pkgname = "kunitconversion"
pkgver = "6.19.0"
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
sha256 = "d4f0e39e27596c6550f3fc72fb67b0d4966acfd7d702a011a0fca420b6f9b393"
hardening = ["vis"]


@subpackage("kunitconversion-devel")
def _(self):
    return self.default_devel()
