pkgname = "wl-mirror"
pkgver = "0.16.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DINSTALL_EXAMPLE_SCRIPTS=ON",
    "-DINSTALL_DOCUMENTATION=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "scdoc", "wayland-progs"]
makedepends = ["mesa-devel", "wayland-devel", "wayland-protocols"]
pkgdesc = "Wayland output mirror client"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/Ferdi265/wl-mirror"
source = f"{url}/releases/download/v{pkgver}/wl-mirror-{pkgver}.tar.gz"
sha256 = "ea7aab751de2a176c115af75fd3594c3a461efe2ffbfd2ffac085ff3f5b9c65c"
