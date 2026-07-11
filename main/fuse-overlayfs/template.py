pkgname = "fuse-overlayfs"
pkgver = "1.17"
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
sha256 = "cefffecfbb001b2784f19af344f27eae07b31a4faa38d345b738af96b2bec59e"
hardening = ["vis", "cfi"]
