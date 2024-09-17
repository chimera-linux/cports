pkgname = "erofs-utils"
pkgver = "1.8.1"
pkgrel = 2
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
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 AND GPL-2.0-or-later"
url = "https://github.com/erofs/erofs-utils"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5dbf7b492f7682462b97a77121d43ca7609cd90e65f8c96931aefc820a6f0da3"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
