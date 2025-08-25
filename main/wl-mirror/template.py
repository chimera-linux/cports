pkgname = "wl-mirror"
pkgver = "0.18.3"
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
sha256 = "52c15744ed2aee1aadb690bce91af49312cae0ed2f514d23bfbfaf0548dbac44"
