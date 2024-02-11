pkgname = "wlopm"
pkgver = "0.1.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
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
sha256 = "f9a7ec03a412e602420ab11d0eea872f6d30dfe5cfee93cd3d0289e4fbbb3aa1"
hardening = ["vis", "cfi"]
# No tests exist
options = ["!check"]
