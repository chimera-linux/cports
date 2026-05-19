pkgname = "fuse-overlayfs"
pkgver = "1.16"
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
sha256 = "45968517603389ead067222d234bc8d8ed33e4b4f8ba16216bdd3e6aedcccea9"
hardening = ["vis", "cfi"]
