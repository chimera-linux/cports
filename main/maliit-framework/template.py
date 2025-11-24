pkgname = "maliit-framework"
pkgver = "2.3.0"
pkgrel = 6
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON", "-Denable-docs=OFF"]
# testLoadPlugins() segfaults but works on runtime?
make_check_args = ["-E", "ft_mimpluginmanager"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "extra-cmake-modules",
    "libxcb-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Core libraries and server of Maliit input method framework"
license = "LGPL-2.1-only"
url = "https://github.com/maliit/framework"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "bfc23919ac8b960243f85e8228ad7dfc28d557b52182a0b5a2a216a5c6a8057c"
tool_flags = {
    "CXXFLAGS": [
        # avoid 2.6k lines of spam
        "-Wno-inconsistent-missing-override",
        "-Wno-deprecated-declarations",
    ]
}


@subpackage("maliit-framework-devel")
def _(self):
    return self.default_devel()
