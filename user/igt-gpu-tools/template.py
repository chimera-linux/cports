pkgname = "igt-gpu-tools"
pkgver = "1.29"
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
    "libdrm-devel",
    "libkmod-devel",
    "pixman-devel",
    "procps-devel",
]
pkgdesc = "Tooling for Intel GPUs"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://gitlab.freedesktop.org/drm/igt-gpu-tools"
source = f"{url}/-/archive/v{pkgver}.tar.gz"
sha256 = "e324d9907a6ab55ecb68cccadbb8146d929b6a3de6af65dc560a4cdeb3ca4a80"
# need fancy setup for integration tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("igt-gpu-tools-devel")
def _(self):
    return self.default_devel()
