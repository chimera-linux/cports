pkgname = "ryzenadj"
pkgver = "0.16.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-only"
url = "https://github.com/FlyGoat/RyzenAdj"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7bef7dbde006afbe316091d8da8c8c551d5d7d43185d9e62281671959b7a3ca2"
