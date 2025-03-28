pkgname = "erofs-utils"
pkgver = "1.8.5"
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
sha256 = "cd8611270e9c86fe062f647103ca6ada9ed710e4430fdd5960d514777919200d"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
