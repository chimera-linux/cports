pkgname = "fcitx5-gtk"
pkgver = "5.1.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_GTK2_IM_MODULE=OFF",
    "-DENABLE_GTK3_IM_MODULE=ON",
    "-DENABLE_GTK4_IM_MODULE=ON",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gobject-introspection",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "gtk4-devel",
    "libxkbcommon-devel",
]
pkgdesc = "Gtk library and IM module for Fcitx5"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://fcitx-im.org"
source = (
    f"https://github.com/fcitx/fcitx5-gtk/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "1892fcaeed0e710cb992a87982a8af78f9a9922805a84da13f7e3d416e2a28d1"
# gobject-introspection
options = ["!cross"]


@subpackage("fcitx5-gtk-devel")
def _devel(self):
    return self.default_devel()


@subpackage("fcitx5-gtk3")
def _gtk3(self):
    self.subdesc = "GTK+3 variant"
    self.install_if = [self.parent, "gtk+3"]

    return [
        "usr/bin/fcitx5-gtk3-immodule-probing",
        "usr/lib/gtk-3.0",
    ]


@subpackage("fcitx5-gtk4")
def _gtk4(self):
    self.subdesc = "GTK4 variant"
    self.install_if = [self.parent, "gtk4"]

    return [
        "usr/bin/fcitx5-gtk4-immodule-probing",
        "usr/lib/gtk-4.0",
    ]
