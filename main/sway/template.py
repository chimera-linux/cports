pkgname = "sway"
pkgver = "1.12_rc1"
pkgrel = 0
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
    "pango-devel",
    "pcre2-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
]
depends = ["xwayland"]
pkgdesc = "Wayland compositor compatible with i3"
license = "MIT"
url = "https://swaywm.org"
source = f"https://github.com/swaywm/sway/releases/download/{pkgver.replace('_', '-')}/sway-{pkgver.replace('_', '-')}.tar.gz"
sha256 = "912554cba209aeea32ef6ccbc1636e7942e92f0ea2d9b3e6d49787649e931226"
file_modes = {
    "usr/bin/sway": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/sway": {
        "security.capability": "cap_sys_nice+ep",
    },
}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "sway-portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("sway-backgrounds")
def _(self):
    self.subdesc = "backgrounds"
    self.install_if = [self.parent]

    return ["usr/share/backgrounds"]
