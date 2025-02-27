pkgname = "sccache"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
make_build_args = []
make_install_args = []
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "openssl3-devel",
    "rust-std",
    "zstd-devel",
]
pkgdesc = "Compilation caching tool with Rust support"
license = "Apache-2.0"
url = "https://github.com/mozilla/sccache"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2c9f82c43ce6a1b1d9b34f029ce6862bedc2f01deff45cde5dffc079deeba801"
# fails due to comparing ldd output to a glibc bin
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"

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
