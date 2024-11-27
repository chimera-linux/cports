pkgname = "swayfx"
pkgver = "0.4"
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
    "wlroots0.17-devel",
]
depends = ["!sway"]
pkgdesc = "Fork of sway with more graphical effects"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/WillPower3309/swayfx"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    # until 1.0
    "https://github.com/wlrfx/scenefx/archive/refs/tags/0.1.tar.gz",
]
source_paths = [".", "subprojects/scenefx"]
sha256 = [
    "fa164734a7b32fd82f31e54c407b147e92247ef275de9df4a87b6198a36f20e2",
    "f5c889f4c826a4216628bf1e7e48071fc33e7774b5e3d51e6fee6e571e420827",
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
