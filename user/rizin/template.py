pkgname = "rizin"
pkgver = "0.7.3"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    # disabled below
    "-Denable_rz_test=false",
    "-Denable_tests=false",
    f"-Dpackager_version={pkgver}-r{pkgrel}",
    "-Dpackager=Chimera Linux",
    "-Duse_sys_capstone=enabled",
    "-Duse_sys_libmspack=enabled",
    "-Duse_sys_libzip=enabled",
    "-Duse_sys_libzstd=enabled",
    "-Duse_sys_lz4=enabled",
    "-Duse_sys_lzma=enabled",
    "-Duse_sys_magic=enabled",
    "-Duse_sys_openssl=enabled",
    "-Duse_sys_pcre2=enabled",
    "-Duse_sys_tree_sitter=enabled",
    "-Duse_sys_xxhash=enabled",
    "-Duse_sys_zlib=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "python-pyyaml",
]
makedepends = [
    "capstone-devel",
    "file-devel",
    "libmspack-devel",
    "libuv-devel",
    "libzip-devel",
    "linux-headers",
    "lz4-devel",
    "openssl-devel",
    "pcre2-devel",
    "tree-sitter-devel",
    "xxhash-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Reverse engineering framework and tooling"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later"
url = "https://rizin.re"
source = f"https://github.com/rizinorg/rizin/releases/download/v{pkgver}/rizin-src-v{pkgver}.tar.xz"
sha256 = "e0ed25ada6be42098d38da9ccef4befbd549e477e80f8dffa5ca1b8ff9fbda74"
# int: breaks some tests
hardening = ["!int"]
# missing test files in release tarball
options = ["!check"]


@subpackage("rizin-devel")
def _(self):
    return self.default_devel()
