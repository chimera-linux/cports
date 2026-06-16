pkgname = "kguiaddons"
pkgver = "6.27.0"
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
url = "https://api.kde.org/frameworks/kguiaddons/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kguiaddons-{pkgver}.tar.xz"
sha256 = "29b043480c45d3e51c57cac74fd83589cc7729c907a6585b72880cbf07feaf82"
hardening = ["vis"]


@subpackage("kguiaddons-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
