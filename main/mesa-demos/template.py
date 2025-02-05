pkgname = "mesa-demos"
pkgver = "9.0.0"
pkgrel = 3
build_style = "meson"
configure_args = [
    "-Dlibdrm=enabled",
    "-Dx11=enabled",
    "-Dwayland=enabled",
    "-Dwith-system-data-files=true",
]
hostmakedepends = [
    "glslang-progs",
    "meson",
    "pkgconf",
    "wayland-progs",
    "wayland-protocols",
]
makedepends = [
    "freeglut-devel",
    "glew-devel",
    "libdecor-devel",
    "libx11-devel",
    "libxext-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
]
depends = [self.with_pkgver("mesa-demos-core")]
pkgdesc = "Collection of OpenGL and Mesa demos and test programs"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://gitlab.freedesktop.org/mesa/demos"
source = f"{url}/-/archive/mesa-demos-{pkgver}/demos-mesa-demos-{pkgver}.tar.gz"
sha256 = "f8884ea0e130c12f752a039dfa96c2f714201e28753077878df6879f89f46680"
options = ["!distlicense"]


def post_install(self):
    # conflicts with util-linux
    self.uninstall("usr/bin/line")


@subpackage("mesa-demos-core")
def _(self):
    self.subdesc = "most useful utilities"
    self.provides = [self.with_pkgver("mesa-utils")]

    return [
        "usr/bin/egl*",
        "usr/bin/es2*",
        "usr/bin/glx*",
        "usr/bin/peglgears",
        "usr/bin/vkgears",
        "usr/bin/xeglgears",
        "usr/bin/xeglthreads",
        "usr/share/mesa-demos",
    ]
