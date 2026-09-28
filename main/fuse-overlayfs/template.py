pkgname = "fuse-overlayfs"
pkgver = "1.18"
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
license = "GPL-2.0-or-later"
url = "https://github.com/containers/fuse-overlayfs"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fdd1896c8de35a15eb14444d7880be81d635fcbbc4ad162d8bc3ccf5627aa8c7"
hardening = ["vis", "cfi"]
