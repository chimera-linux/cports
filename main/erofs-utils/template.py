pkgname = "erofs-utils"
pkgver = "1.8.10"
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
    "linux-headers",
    "lz4-devel",
    "util-linux-uuid-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Userspace tools for the EROFS filesystem"
license = "Apache-2.0 AND GPL-2.0-or-later"
url = "https://github.com/erofs/erofs-utils"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "05eb4edebe11decce6ecb34e98d2f80c8cd283c2f2967d8ba7efd58418570514"
tool_flags = {
    "CFLAGS": ["-D_LARGEFILE64_SOURCE"],
    "LDFLAGS": ["-Wl,-z,stack-size=2097152"],
}
