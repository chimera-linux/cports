pkgname = "mesa-demos"
pkgver = "9.0.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlibdrm=enabled", "-Dx11=enabled",
    "-Dwayland=enabled", "-Dwith-system-data-files=true"
]
hostmakedepends = [
    "pkgconf", "meson", "wayland-protocols", "wayland-progs",
    "glslang-progs",
]
makedepends = [
    "mesa-devel", "glew-devel", "freeglut-devel", "wayland-devel",
    "vulkan-headers", "vulkan-loader", "libxkbcommon-devel",
    "libx11-devel", "libxext-devel", "libdecor-devel",
]
depends = [f"mesa-utils={pkgver}-r{pkgrel}"]
pkgdesc = "Collection of OpenGL and Mesa demos and test programs"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://gitlab.freedesktop.org/mesa/demos"
source = f"{url}/-/archive/{pkgname}-{pkgver}/demos-{pkgname}-{pkgver}.tar.gz"
sha256 = "f8884ea0e130c12f752a039dfa96c2f714201e28753077878df6879f89f46680"

@subpackage("mesa-utils")
def _utils(self):
    self.pkgdesc = "Common Mesa utilities"

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
