pkgname = "wl-mirror"
pkgver = "0.16.3"
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
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "cf3cdf97caaf799cb4c780ec931f8a56a4b48274fc1d910e080ce8df1f68a818"
# no tests defined
options = ["!check"]
