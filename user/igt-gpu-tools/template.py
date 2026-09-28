pkgname = "igt-gpu-tools"
pkgver = "2.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dtests=disabled",
    "-Drunner=disabled",
]
hostmakedepends = [
    "bash",
    "bison",
    "flex",
    "meson",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "elfutils-devel",
    "kmod-devel",
    "libdrm-devel",
    "pciutils-devel",
    "pixman-devel",
]
pkgdesc = "Tooling for Intel GPUs"
license = "MIT"
url = "https://gitlab.freedesktop.org/drm/igt-gpu-tools"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "3f3afa417bfec25299c24ee9f35ff6ad3d05e699b28b644eefd4e804754c6d51"
# need fancy setup for integration tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("igt-gpu-tools-devel")
def _(self):
    return self.default_devel()
