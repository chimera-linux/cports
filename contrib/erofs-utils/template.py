pkgname = "erofs-utils"
pkgver = "1.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-fuse"]
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "fuse-devel",
    "libuuid-devel",
    "linux-headers",
    "lz4-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Userspace tools for the EROFS filesystem"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 AND GPL-2.0-or-later"
url = "https://github.com/erofs/erofs-utils"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "117f9e5d9411e8188abb6bf77d9fa967291f60a9ee65f3dcb8e9f88e5307afdf"
