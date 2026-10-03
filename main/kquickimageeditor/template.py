pkgname = "kquickimageeditor"
pkgver = "0.7.0.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "highway-devel",
    "kconfig-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "QML image editing components"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/libraries/kquickimageeditor"
source = f"$(KDE_SITE)/kquickimageeditor/kquickimageeditor-{pkgver}.tar.xz"
sha256 = "b65f32c44bd126cea5e1b5a6eb7cb0eb517277cb8de06675fa6be624b7da381a"

if self.profile.arch == "x86_64":
    # stackblur segfaults with sse4 and above; this disables dynamic
    # displatch so we only select the sse2 baseline target which works
    tool_flags = {"CXXFLAGS": ["-DHWY_COMPILE_ONLY_STATIC"]}


@subpackage("kquickimageeditor-devel")
def _(self):
    return self.default_devel()
