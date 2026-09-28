pkgname = "rizin"
pkgver = "0.9.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    f"-Dpackager_version={pkgver}-r{pkgrel}",
    "-Dpackager=Chimera Linux",
    "-Duse_sys_blake3=enabled",
    "-Duse_sys_capstone=enabled",
    "-Duse_sys_magic=enabled",
    "-Duse_sys_libmspack=enabled",
    "-Duse_sys_libzip=enabled",
    "-Duse_sys_lzma=enabled",
    "-Duse_sys_zlib=enabled",
    "-Duse_sys_lz4=enabled",
    "-Duse_sys_libzstd=enabled",
    "-Duse_sys_xxhash=enabled",
    "-Duse_sys_openssl=enabled",
    "-Duse_sys_pcre2=enabled",
    "-Duse_sys_tree_sitter=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "python-pyyaml",
]
makedepends = [
    "blake3-devel",
    "capstone-devel",
    "file-devel",
    "libmspack-devel",
    "libzip-devel",
    "linux-headers",
    "lz4-devel",
    "openssl3-devel",
    "pcre2-devel",
    "tree-sitter-devel",
    "xxhash-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Reverse engineering framework"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later"
url = "https://rizin.re"
source = f"https://github.com/rizinorg/rizin/releases/download/v{pkgver}/rizin-src-v{pkgver}.tar.xz"
sha256 = "7ac1cd7daca7afdda742e15478b1f747fc1f813e496fee71839d1e109e543dca"
# breaks some tests
hardening = ["!int"]
# needs separate test bins, unstable
options = ["!check"]


@subpackage("rizin-devel")
def _(self):
    return self.default_devel()
