pkgname = "wayfire"
pkgver = "0.8.0"
pkgrel = 4
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
    "wlroots-devel",
]
pkgdesc = "Modular and extensible wayland compositor"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wayfire/releases/download/v{pkgver}/wayfire-{pkgver}.tar.xz"
sha256 = "6e6af885c08822e3a0b1fd748e1ee75e29bc000e376f6613b26c564f8cbc2baf"
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
    # libwayfire-blur-base.so should remain in main package
    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/libwf-utils.so",
        "usr/lib/pkgconfig",
    ]
