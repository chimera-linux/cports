pkgname = "igt-gpu-tools"
pkgver = "1.30"
pkgrel = 1
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/drm/igt-gpu-tools"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "a3e61ac583fb7849e9543ba5e74b86b68baa3b902702c9f507c9956763a46bb9"
# need fancy setup for integration tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("igt-gpu-tools-devel")
def _(self):
    return self.default_devel()
