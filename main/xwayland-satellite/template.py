pkgname = "xwayland-satellite"
pkgver = "0.5"
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
sha256 = "b0845b711750b9850b87d8a62fd7d9a07235fe63a3b7e5bdd727884c066f1b4c"
# no idea how to run this
options = ["!check"]
