pkgname = "wayfire"
pkgver = "0.11.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Duse_system_wfconfig=enabled",
    "-Duse_system_wlroots=enabled",
    "-Dxwayland=enabled",
]
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "glm",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libxml2-devel",
    "nlohmann-json",
    "pango-devel",
    "udev-devel",
    "wayland-protocols",
    "wf-config-devel",
    "wlroots0.20-devel",
    "yyjson-devel",
]
pkgdesc = "Modular and extensible wayland compositor"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wayfire/releases/download/v{pkgver}/wayfire-{pkgver}.tar.xz"
sha256 = "29dc95468c4f954341c9ecbad889b661eb849bdb96fb47e19c9d6edc8d49640b"
# vis breaks symbols
hardening = ["!vis"]
# FIXME: crashes in signal-provider.hpp::provider_t::emit from libblur
# probably since clang17
options = ["!lto"]

if self.profile().arch in [
    "aarch64",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "riscv64",
    "x86_64",
]:
    makedepends += ["libomp-devel"]
else:
    configure_args += ["-Denable_openmp=false"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wayfire-devel")
def _(self):
    return self.default_devel()
