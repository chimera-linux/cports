pkgname = "xwayland-satellite"
pkgver = "0.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "libxcb-devel",
    "rust-std",
    "xcb-util-cursor-devel",
    "xwayland-devel",
]
depends = ["xwayland"]
pkgdesc = "Xwayland manager for Wayland"
maintainer = "psykose <alice@ayaya.dev>"
license = "MPL-2.0"
url = "https://github.com/Supreeeme/xwayland-satellite"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0c1db058f87a7ab686778c77bc0182ff5220fdbc3558706ea86ea7b955ea271e"
# no idea how to run this
options = ["!check"]
