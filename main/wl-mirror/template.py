pkgname = "wl-mirror"
pkgver = "0.18.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DINSTALL_EXAMPLE_SCRIPTS=ON",
    "-DINSTALL_DOCUMENTATION=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "scdoc", "wayland-progs"]
makedepends = ["mesa-devel", "wayland-devel", "wayland-protocols"]
pkgdesc = "Wayland output mirror client"
license = "GPL-3.0-or-later"
url = "https://github.com/Ferdi265/wl-mirror"
source = f"{url}/releases/download/v{pkgver}/wl-mirror-{pkgver}.tar.gz"
sha256 = "2b3e70374a229cdf49b421c75ce8974f1f666ba8c6a546b0cf88f550f118ba60"
