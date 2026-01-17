pkgname = "wayfire"
pkgver = "0.10.0"
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
    "libxml2-devel",
    "nlohmann-json",
    "pango-devel",
    "wayland-protocols",
    "wf-config-devel",
    "wlroots0.19-devel",
    "yyjson-devel",
]
pkgdesc = "Modular and extensible wayland compositor"
license = "MIT"
url = "https://wayfire.org"
source = f"https://github.com/WayfireWM/wayfire/releases/download/v{pkgver}/wayfire-{pkgver}.tar.xz"
sha256 = "83f98d67479f41f3a4dcf30b414495bb8df2353daa7601159f4012a120827a16"
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
