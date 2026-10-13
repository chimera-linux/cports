pkgname = "kguiaddons"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
# unpackaged pyside6
configure_args = ["-DBUILD_PYTHON_BINDINGS=OFF"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = [
    "plasma-wayland-protocols",
    "qt6-qtbase-private-devel",  # qtguiglobal_p.h
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
]
pkgdesc = "KDE addons to QtGui"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kguiaddons-{pkgver}.tar.xz"
sha256 = "d440bbe350282b03c828d5987a6db1f0a4f5d87a528907bf19e1e5bb76d4b219"
hardening = ["vis"]


@subpackage("kguiaddons-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
