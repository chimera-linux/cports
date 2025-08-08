pkgname = "kjobwidgets"
pkgver = "6.17.0"
pkgrel = 0
build_style = "cmake"
# unpackaged pyside6
configure_args = ["-DBUILD_PYTHON_BINDINGS=OFF"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = [
    "kcoreaddons-devel",
    "knotifications-devel",
    "kwidgetsaddons-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qttools-devel",
]
pkgdesc = "KDE Widgets for showing progress of asynchronous jobs"
license = "LGPL-2.1-only AND (LGPL-2.1-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/kjobwidgets/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kjobwidgets-{pkgver}.tar.xz"
sha256 = "0dc56de19bce3769b78c34dab1399588017180f298de8419eda1909a4211b624"
hardening = ["vis"]


@subpackage("kjobwidgets-devel")
def _(self):
    return self.default_devel()
