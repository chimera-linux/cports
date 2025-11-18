pkgname = "scroll"
pkgver = "1.11.8"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "libcap-progs",
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "json-c-devel",
    "lua5.4-devel",
    "pango-devel",
    "pcre2-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.19-devel",
]
depends = ["xwayland"]
pkgdesc = "Wayland compositor forked from sway, with a scrolling layout only"
license = "MIT"
url = "https://github.com/dawsers/scroll"
source = f"https://github.com/dawsers/scroll/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d44cfac63c67546c0651dd637902fb294144611ab7dfcf82ac550dd6696049f3"
file_modes = {
    "usr/bin/scroll": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/scroll": {
        "security.capability": "cap_sys_nice+ep",
    },
}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "scroll-portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("scroll-backgrounds")
def _(self):
    self.subdesc = "backgrounds"
    self.install_if = [self.parent]

    return ["usr/share/backgrounds"]
