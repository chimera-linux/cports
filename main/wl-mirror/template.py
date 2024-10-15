pkgname = "wl-mirror"
pkgver = "0.17.0"
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
sha256 = "01a0874b7a5fbda3995f6b4a8a5e58cae2471229d28366896edd57548b2d4eca"
