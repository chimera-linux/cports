pkgname = "xwayland-satellite"
pkgver = "0.8.1"
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
sha256 = "44d4ed941f99b88be6655d9c31db90d2a44e2deec52da7446237354508369caf"
# no idea how to run this
options = ["!check"]
