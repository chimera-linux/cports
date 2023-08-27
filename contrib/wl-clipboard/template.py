pkgname = "wl-clipboard"
pkgver = "2.2.1"
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
sha256 = "6eb8081207fb5581d1d82c4bcd9587205a31a3d47bea3ebeb7f41aa1143783eb"
hardening = ["vis", "!cfi"]
