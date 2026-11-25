pkgname = "swayfx"
pkgver = "0.6"
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
    "pango-devel",
    "pcre2-devel",
    "scenefx-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
]
depends = ["!sway"]
pkgdesc = "Fork of sway with more graphical effects"
license = "MIT"
url = "https://github.com/WillPower3309/swayfx"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "854f9d1468b8706718210e026d0bb0ddbc8370f750345fbbdd163f130c1b922d"
file_modes = {
    "usr/bin/sway": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/sway": {
        "security.capability": "cap_sys_nice+ep",
    },
}
options = ["etcfiles"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "sway-portals.conf", "usr/share/xdg-desktop-portal"
    )
    # same as main sway
    self.uninstall("usr/share/backgrounds")
