pkgname = "wl-clipboard"
pkgver = "2.3.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = ["wayland-devel", "wayland-protocols"]
depends = ["xdg-utils"]
pkgdesc = "Command-line copy/paste utilities for Wayland"
license = "GPL-3.0-or-later"
url = "https://github.com/bugaevc/wl-clipboard"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b4dc560973f0cd74e02f817ffa2fd44ba645a4f1ea94b7b9614dacc9f895f402"
hardening = ["vis", "!cfi"]
