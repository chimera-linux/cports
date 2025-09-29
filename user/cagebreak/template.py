pkgname = "cagebreak"
pkgver = "3.1.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dman-pages=true", "-Dxwayland=true", "--buildtype=release"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
    "wayland",
]
makedepends = [
    "cairo-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.19-devel",
]
depends = ["wayland", "libxkbcommon", "wlroots0.19", "pango-view"]
pkgdesc = "Wayland Tiling Compositor inspred by Ratpoison"
license = "MIT"
url = "https://github.com/project-repo/cagebreak"
source = f"https://github.com/project-repo/cagebreak/releases/download/{pkgver}/release_{pkgver}.tar.gz"
sha256 = "2b62c32da739668f0d99e41144ad721c0fc02b184a9c451458644071bb335770"
# check requires
# a) gsed dep, patching tests to use that with shopt -s expand_aliases,
#    alias sed=gsed
# b) patching some bad paths in test/arguments ~> build-arguments{/,}
# c) patching missing XDG_RUNTIME_DIR=$(pwd)
# fixing the above is not worth it downstream because:
# d) it still doesn't work because missing drm backend in bldroot so wlroots
#    explodes, and well i think all hope is lost to test this in cbuild
# this would also only be the basic test suite.
# !check is the reason for no hardening opts
options = ["!check"]


def post_install(self):
    self.install_file("examples/config", "usr/share/etc/cagebreak")
