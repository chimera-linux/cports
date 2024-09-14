pkgname = "lswt"
pkgver = "2.0.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "wayland-progs",
]
makedepends = [
    "linux-headers",
    "wayland-devel",
]
pkgdesc = "List Wayland toplevels"
maintainer = "Hugo Machet <mail@hmachet.com>"
license = "GPL-3.0-only"
url = "https://git.sr.ht/~leon_plickat/lswt"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8e23cc5c00bb715b0a1610938111cb76eb9efe1eea87408123620a8a7155e6ab"
hardening = ["vis", "cfi"]
# No tests exist
options = ["!check"]
