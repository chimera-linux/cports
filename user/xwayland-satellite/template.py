pkgname = "xwayland-satellite"
pkgver = "0.6"
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
sha256 = "81d23bf4b75e841f14039efc0b2b1a0ffa81ed6715ca21339d63423e056ccb25"
# no idea how to run this
options = ["!check"]
