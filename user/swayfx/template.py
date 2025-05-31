pkgname = "swayfx"
pkgver = "0.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=static", "-Dscenefx:examples=false"]
make_install_args = ["--skip-subprojects"]
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
depends = ["!sway"]
pkgdesc = "Fork of sway with more graphical effects"
license = "MIT"
url = "https://github.com/WillPower3309/swayfx"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    # until 1.0
    "https://github.com/wlrfx/scenefx/archive/refs/tags/0.2.1.tar.gz",
]
source_paths = [".", "subprojects/scenefx"]
sha256 = [
    "68bff05a89da702bbca7df3c5c633a149cc59e9e8158c1bd60f0e9fe768f86b3",
    "e50cd8cbeb6564233dced39f21e78d755701fa7fe67f5b354f033f397b69a2b8",
]
file_modes = {
    "usr/bin/sway": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/sway": {
        "security.capability": "cap_sys_nice+ep",
    },
}


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "sway-portals.conf", "usr/share/xdg-desktop-portal"
    )
    # same as main sway
    self.uninstall("usr/share/backgrounds")
