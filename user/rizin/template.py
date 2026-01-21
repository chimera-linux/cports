pkgname = "rizin"
pkgver = "0.8.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Duse_sys_magic=enabled",
    "-Duse_sys_libzip=enabled",
    "-Duse_sys_lzma=enabled",
    "-Duse_sys_zlib=enabled",
    "-Duse_sys_lz4=enabled",
    "-Duse_sys_libzstd=enabled",
    "-Duse_sys_xxhash=enabled",
    "-Duse_sys_openssl=enabled",
    "-Duse_sys_libmspack=enabled",
    "-Duse_sys_pcre2=enabled",
    "-Duse_sys_tree_sitter=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "file-devel",
    "libzip-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "lz4-devel",
    "zstd-devel",
    "xxhash-devel",
    "openssl3-devel",
    "libmspack-devel",
    "pcre2-devel",
    "tree-sitter-devel",

    "linux-headers",
]
pkgdesc = "Free and Open Source Reverse Engineering Framework"
license = "LGPL-3.0-only"
url = "https://rizin.re"
source = [
    f"https://github.com/rizinorg/rizin/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/rizinorg/rz-libdemangle/archive/d3083c18befed11069b65c57c2ad79fa5d9afba4.tar.gz",
    "https://github.com/BLAKE3-team/BLAKE3/archive/2de3cb1a21d09cdee4c8b6b14513063198cf1b82.tar.gz",
    "https://github.com/rizinorg/rizin-grammar-c/archive/815845762d59f727d79e7aa6f810688b2e1e35d2.tar.gz",
    "https://github.com/rizinorg/softfloat/archive/537d18e71a51aea70f6b54334854f7014c6458c7.tar.gz",
    "https://github.com/capstone-engine/capstone/archive/895f2f2e10c245a45880c07c2666d498e62d8ecf.tar.gz",

    # rizin-testbins is only needed for tests
    "https://github.com/rizinorg/rizin-testbins/archive/71482f7194847b4ece45a9e53f28085b6bab40a4.tar.gz",
]
source_paths = [
    ".",
    "subprojects/libdemangle",
    "subprojects/packagecache/blake3",
    "subprojects/packagecache/rizin-grammar-c",
    "subprojects/softfloat",
    "subprojects/packagecache/capstone-next",

    # rizin-testbins is only needed for tests
    "test/bins",
]
sha256 = [
    "7dc451968f426e846c04430f7d6d45f1402db8eed1afa902f0631c03f19bc22e",
    "1476a55dd22fc78ce62e2035910a39f318d603ef1c1d27eadc71eb25c645739f",
    "175e6b5edcae9044e33ad14bdb90810de3571c1fff21fd12fa1aed600de3e928",
    "d382799c5c66846d398c4e371579155180c305a3c5d66961556478095151ea1e",
    "b0a7ae06352f0b0cfab2b9ccb23793ce8028b5ad065d5f1ab25714ac746fc68e",
    "e4ee5c5000b6f3066633c154622f3ad27e4f9a8675c4e59f716bd3993d359ddd",

    # rizin-testbins is only needed for tests
    "0555dfb089df632a3c4353da341f1fd5f7724dcbaffc9db6d250caf5d9636a21",
]

# Summary of Failures:
#
#  11/126 rizin:unit / analysis_var                          FAIL            0.06s   killed by signal 4 SIGILL
#  51/126 rizin:unit / inflate_deflate                       FAIL            0.08s   exit status 1
# 124/126 rizin:integration / dwarf_integration              FAIL            0.88s   exit status 1
#
# Ok:                123
# Fail:              3
options = ["!check"]

@subpackage("rizin-devel")
def _(self):
    return self.default_devel()
