pkgname = "kguiaddons"
pkgver = "6.29.0"
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
sha256 = "6d0c4a4ddc7d4833ae537b1bf146896beba76135ec4b8bcf2a9525e33e39b3a4"
hardening = ["vis"]


@subpackage("kguiaddons-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
