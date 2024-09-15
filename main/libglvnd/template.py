pkgname = "libglvnd"
pkgver = "1.7.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dglx=enabled", "-Dtls=false", "-Dx11=enabled"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libxext-devel", "libx11-devel"]
pkgdesc = "GL Vendor-Neutral Dispatch Library"
maintainer = "mizz1e <158266562+mizz1e@users.noreply.github.com>"
license = "MIT"
url = "https://gitlab.freedesktop.org/glvnd/libglvnd"
source = f"{url}/-/archive/v{pkgver}/libglvnd-v{pkgver}.tar.bz2"
sha256 = "d0e1925a3c9aee0143b8c181ac31d5637c8faa081759c277b8e16c7075612c11"
# unknown exported symbols (libgcc backtraces), and cannot open display (needs an x server)
options = ["!check"]

def post_install(self):
    self.install_license("README.md")

@subpackage("libglvnd-devel")
def _(self):
    return self.default_devel()

@subpackage("libgles1")
def _(self):
    self.pkgdesc = "Free implementation of OpenGL ES 1.x API"
    self.subdesc = "runtime library"
    self.depends += [self.parent]

    return ["usr/lib/libGLESv1_CM.so.*"]


@subpackage("libgles2")
def _(self):
    self.pkgdesc = "Free implementation of OpenGL ES 2.x API"
    self.subdesc = "runtime library"
    self.depends += [self.parent]

    return ["usr/lib/libGLESv2.so.*"]


@subpackage("libegl")
def _(self):
    self.pkgdesc = "Free implementation of the EGL API"
    self.subdesc = "runtime library"
    self.depends += [self.parent]

    return ["usr/lib/libEGL.so.*"]
