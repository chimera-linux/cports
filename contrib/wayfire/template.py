pkgname = "wayfire"
pkgver = "0.8.1"
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
    "nlohmann-json",
    "pango-devel",
    "wayland-protocols",
    "wf-config-devel",
    "wlroots0.17-devel",
]
pkgdesc = "Modular and extensible wayland compositor"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wayfire/releases/download/v{pkgver}/wayfire-{pkgver}.tar.xz"
sha256 = "8ac1947b688a9ec6c4d9ee2d77311bb357a8ead25665b8000eda96952328290d"
# vis breaks symbols
hardening = ["!vis"]
# FIXME: crashes in signal-provider.hpp::provider_t::emit from libblur
# probably since clang17
options = ["!lto"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "wayfire-portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("wayfire-devel")
def _devel(self):
    return self.default_devel()
