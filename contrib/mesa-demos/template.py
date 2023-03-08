pkgname = "mesa-demos"
pkgver = "8.5.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dlibdrm=enabled", "-Dx11=enabled", "-Dwayland=enabled", "-Dwith-system-data-files=true"]
hostmakedepends = ["pkgconf", "meson", "wayland-protocols", "wayland-progs"]
makedepends = ["mesa-devel", "glew-devel", "freeglut-devel", "wayland-devel"]
pkgdesc = "Collection of OpenGL / Mesa demos and test programs"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://gitlab.freedesktop.org/mesa/demos"
source = f"https://gitlab.freedesktop.org/mesa/demos/-/archive/mesa-demos-{pkgver}/demos-mesa-demos-{pkgver}.tar.gz"
sha256 = "0dda2c6199de61798ff1c00ab135823fe06ada077b94e99a430347efd8c28634"


@subpackage("glxinfo")
def _glxinfo(self):
    return ["usr/bin/glxinfo"]


@subpackage("glxgears")
def _glxgears(self):
    return ["usr/bin/glxgears*"]
