pkgname = "erofs-utils"
pkgver = "1.8.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-fuse",
    "--enable-multithreading",
    "--with-libdeflate",
    "--with-libzstd",
    "--with-uuid",
    "--with-zlib",
]
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "fuse-devel",
    "libdeflate-devel",
    "libuuid-devel",
    "linux-headers",
    "lz4-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Userspace tools for the EROFS filesystem"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0 AND GPL-2.0-or-later"
url = "https://github.com/erofs/erofs-utils"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3c5cc03603ea08ba9ae5e0420eeaea5ff17ed29e2280685310356cbf25304e85"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
