pkgname = "fuse-overlayfs"
pkgver = "1.13"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "fuse-devel",
    "linux-headers",
]
pkgdesc = "FUSE implementation for overlayfs"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/containers/fuse-overlayfs"
source = f"https://github.com/containers/fuse-overlayfs/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "96d10344921d5796bcba7a38580ae14a53c4e60399bb90b238ac5a10b3bb65b2"
hardening = ["vis", "cfi"]
