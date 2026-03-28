pkgname = "sway"
pkgver = "1.12_rc3"
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
sha256 = "ab393b85eefb9d410e8740cc1339d594209b39360547e9ac61b297a7acb8f934"
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
