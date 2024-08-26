pkgname = "egl-wayland"
pkgver = "1.1.16"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["cmake", "meson", "pkgconf"]
makedepends = [
    "eglexternalplatform",
    "libdrm-devel",
    "libglvnd-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Wayland EGL external platform library"
maintainer = "mizz1e <158266562+mizz1e@users.noreply.github.com>"
license = "MIT"
url = "https://github.com/NVIDIA/egl-wayland"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d3302002987128dac159ec5dde7a53831ccb905288daad62d1d18bafa0388858"


def post_install(self):
    self.install_license("COPYING")

    self.rm(self.destdir / "usr/lib/pkgconfig", recursive = True)
    self.rm(self.destdir / "usr/share/pkgconfig", recursive = True)
    self.rm(self.destdir / "usr/share/wayland-eglstream", recursive = True)
