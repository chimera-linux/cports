pkgname = "erofs-utils"
pkgver = "1.8.2"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 AND GPL-2.0-or-later"
url = "https://github.com/erofs/erofs-utils"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "64b6ff7e899f62480283cee63787f37f0f9c4be7a6bc7a23d734aaa873a6cff4"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=2097152"]}
