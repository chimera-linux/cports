pkgname = "sway"
pkgver = "1.10"
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
    "wlroots0.18-devel",
]
pkgdesc = "Wayland compositor compatible with i3"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://swaywm.org"
source = f"https://github.com/swaywm/sway/releases/download/{pkgver}/sway-{pkgver}.tar.gz"
sha256 = "7472a7f11150212e0bed0bd0af9f591c9caac9f9ea87c35486e475a21f5ce81f"
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
