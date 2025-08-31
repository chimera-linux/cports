pkgname = "xwayland-satellite"
pkgver = "0.7"
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
sha256 = "466fc8d44b45f446a581549ab4e55ce65aa32e090e98638dde79f9da9faf89a0"
# no idea how to run this
options = ["!check"]
