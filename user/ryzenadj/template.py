pkgname = "ryzenadj"
pkgver = "0.17.0"
pkgrel = 0
# only for ryzen cpus
archs = ["x86_64"]
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["pciutils-devel"]
pkgdesc = "Adjust power management settings for Ryzen mobile processors"
license = "LGPL-3.0-only"
url = "https://github.com/FlyGoat/RyzenAdj"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "848ac9d86ff65d30f5e2c8600aac2613f0f10003b0d6f0e516a54761d7345d44"
