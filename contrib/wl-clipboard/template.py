pkgname = "wl-clipboard"
pkgver = "2.2.0"
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
maintainer = "Wesley Moore <wes@wezm.net>"
license = "GPL-3.0-or-later"
url = "https://github.com/bugaevc/wl-clipboard"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "414005cfa229d0e54f89a0d9a8473938e4c29adc21a9e556847a4d44ad508874"
hardening = ["vis", "!cfi"]
