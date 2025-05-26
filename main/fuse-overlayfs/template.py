pkgname = "fuse-overlayfs"
pkgver = "1.15"
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
sha256 = "e4fbbdacbeffb560715e6c74c128aee07a7053a1fec78dc904bcc0a88e2efd67"
hardening = ["vis", "cfi"]
