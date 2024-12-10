pkgname = "wlopm"
pkgver = "1.0.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "wayland-progs",
]
makedepends = [
    "wayland-devel",
]
pkgdesc = "Wayland output power management"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "GPL-3.0-only"
url = "https://sr.ht/~leon_plickat/wlopm"
source = f"https://git.sr.ht/~leon_plickat/wlopm/archive/v{pkgver}.tar.gz"
sha256 = "15f31bbd855131943397dded3a26003f2f5056e4c6a1a93d35ff7697b3f1e439"
hardening = ["vis", "cfi"]
# No tests exist
options = ["!check"]
