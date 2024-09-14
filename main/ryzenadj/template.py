pkgname = "ryzenadj"
pkgver = "0.15.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-only"
url = "https://github.com/FlyGoat/RyzenAdj"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5ad53e311ad7e2cc6ddf03787dbba7d7aec64d564b8135cb7d8a1c8bd93779ef"
