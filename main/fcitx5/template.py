pkgname = "fcitx5"
pkgver = "5.1.14"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
    "wayland-progs",
    "wayland-protocols",
]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "enchant-devel",
    "fmt-devel",
    "gdk-pixbuf-devel",
    "gettext-devel",
    "iso-codes",
    "json-c-devel",
    "libuv-devel",
    "libxkbcommon-devel",
    "libxkbfile-devel",
    "linux-headers",
    "pango-devel",
    "wayland-devel",
    "xcb-imdkit-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-wm-devel",
]
pkgdesc = "Generic input method framework"
license = "LGPL-2.1-or-later"
url = "https://fcitx-im.org"
_en_dict_ver = "20121020"
source = [
    f"https://github.com/fcitx/fcitx5/archive/refs/tags/{pkgver}.tar.gz",
    f"!https://download.fcitx-im.org/data/en_dict-{_en_dict_ver}.tar.gz",
]
sha256 = [
    "c81bbf0156d083e4c7e7817e658122c33a8c1e585962467f251bc9614bdfee47",
    "c44a5d7847925eea9e4d2d04748d442cd28dd9299a0b572ef7d91eac4f5a6ceb",
]
# CFI: causes illegal instruction crashes
hardening = ["vis", "!cfi"]


def post_extract(self):
    self.cp(
        self.sources_path / f"en_dict-{_en_dict_ver}.tar.gz",
        "src/modules/spell/",
    )


@subpackage("fcitx5-devel")
def _(self):
    return self.default_devel()


@subpackage("fcitx5-diagnose")
def _(self):
    self.depends = [self.parent, "bash"]
    self.install_if = [self.parent, "bash"]
    return ["cmd:fcitx5-diagnose"]
