pkgname = "wayfire"
pkgver = "0.7.5"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Duse_system_wfconfig=enabled",
    "-Duse_system_wlroots=enabled",
    "-Dxwayland=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "glm",
    "libxml2-devel",
    "pango-devel",
    "wayland-protocols",
    "wf-config-devel",
    "wlroots-devel",
]
pkgdesc = "Modular and extensible wayland compositor"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wayfire/releases/download/v{pkgver}/wayfire-{pkgver}.tar.xz"
sha256 = "f2e3184e72fe7999488fbba10bd38c29350b447489f02961aab5fa8438698b5c"
# vis breaks symbols
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "wayfire-portals.conf", "etc/xdg-desktop-portal"
    )


@subpackage("wayfire-devel")
def _devel(self):
    return self.default_devel()
