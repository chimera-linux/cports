pkgname = "wayfire"
pkgver = "0.9.0"
pkgrel = 0
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
    "libomp-devel",
    "libxml2-devel",
    "nlohmann-json",
    "pango-devel",
    "wayland-protocols",
    "wf-config-devel",
    "wlroots0.17-devel",
]
pkgdesc = "Modular and extensible wayland compositor"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wayfire/releases/download/v{pkgver}/wayfire-{pkgver}.tar.xz"
sha256 = "dd0c9c08b8a72a2d8c3317c8be6c42b17a493c25abab1d02ac09c24eaa95229d"
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
def _(self):
    return self.default_devel()
