pkgname = "poweralertd"
pkgver = "0.2.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = ["elogind-devel"]
depends = ["upower"]
pkgdesc = "UPower-powered power alerter"
maintainer = "Umar Getagazov <umar@handlerug.me>"
license = "GPL-3.0-only"
url = "https://sr.ht/~kennylevinsen/poweralertd"
source = f"https://git.sr.ht/~kennylevinsen/poweralertd/archive/{pkgver}.tar.gz"
sha256 = "f70076dad452c592e2fcdeba4fd533c11394c254f42c21522aa7b56f92a0bd69"
hardening = ["vis", "cfi"]
