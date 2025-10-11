pkgname = "swayfx"
pkgver = "0.5.3"
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
    "wlroots0.19-devel",
]
depends = ["!sway"]
pkgdesc = "Fork of sway with more graphical effects"
license = "MIT"
url = "https://github.com/WillPower3309/swayfx"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    # until 1.0
    "https://github.com/wlrfx/scenefx/archive/refs/tags/0.4.1.tar.gz",
]
source_paths = [".", "subprojects/scenefx"]
sha256 = [
    "e6345e198f128520cf422b458ac8ad9759c3a6c8f633d7b722655309f8a14b9e",
    "fa23f6ff509168d4a5eb0c5a7ef3b8cf3d39e3fba18320c28256e6c91c85d9ff",
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
