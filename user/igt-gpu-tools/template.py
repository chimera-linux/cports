pkgname = "igt-gpu-tools"
pkgver = "2.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
    "pixman-devel",
    "procps-devel",
]
pkgdesc = "Tooling for Intel GPUs"
license = "MIT"
url = "https://gitlab.freedesktop.org/drm/igt-gpu-tools"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "674dd5ee3421e658ae0cf5b12932b07ea9ab47705dc5351ec180a47ab9a2e5dc"
# need fancy setup for integration tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("igt-gpu-tools-devel")
def _(self):
    return self.default_devel()
