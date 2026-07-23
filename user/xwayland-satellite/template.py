pkgname = "xwayland-satellite"
pkgver = "0.8.2"
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
license = "MPL-2.0"
url = "https://github.com/Supreeeme/xwayland-satellite"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cb50bb6948582d5ec3aa511d2d66ad622989bb14bef94e3bb81bae8b64c120b1"
# no idea how to run this
options = ["!check"]
