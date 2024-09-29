pkgname = "tofi"
pkgver = "0.9.1"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
    "wayland-progs",
    "wayland-protocols",
]
makedepends = [
    "cairo-devel",
    "chimerautils-devel",
    "freetype-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Wayland dynamic menu"
maintainer = "jabuxas <jabuxas@proton.me>"
license = "MIT"
url = "https://github.com/philj56/tofi"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dd55347b509af786f133def64f3a86f1db258b5e196de80e53d62827bdcc37bc"
