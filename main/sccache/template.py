pkgname = "sccache"
pkgver = "0.8.2"
pkgrel = 0
build_style = "cargo"
make_build_args = []
make_install_args = []
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "openssl-devel",
    "rust-std",
    "zstd-devel",
]
pkgdesc = "Compilation caching tool with Rust support"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/mozilla/sccache"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2b3e0ef8902fe7bcdcfccf393e29f4ccaafc0194cbb93681eaac238cdc9b94f8"
# fails due to comparing ldd output to a glibc bin
options = ["!check"]

# only supported by upstream on x86_64 linux and freebsd
_have_dist = self.profile().arch == "x86_64"

if _have_dist:
    _eargs = [
        "--no-default-features",
        "--features=all,dist-server",
    ]
    make_build_args += _eargs
    make_install_args += _eargs


@subpackage("sccache-dist", _have_dist)
def _(self):
    self.subdesc = "distributed server"
    return ["usr/bin/sccache-dist"]
