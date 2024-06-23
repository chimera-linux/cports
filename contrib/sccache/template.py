pkgname = "sccache"
pkgver = "0.8.1"
pkgrel = 1
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "openssl-devel",
    "zstd-devel",
]
pkgdesc = "Compilation caching tool with Rust support"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/mozilla/sccache"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "30b951b49246d5ca7d614e5712215cb5f39509d6f899641f511fb19036b5c4e5"
# fails due to comparing ldd output to a glibc bin
options = ["!check"]


# sccache-dist is only supported on x86_64 Linux machines and on FreeBSD
if self.profile().arch == "x86_64":
    make_build_args = [
        "--no-default-features",
        "--features=all,dist-server",
    ]
    make_install_args = make_build_args


@subpackage("sccache-dist", self.profile().arch == "x86_64")
def _dist(self):
    self.pkgdesc = f"{pkgdesc} (distributed server)"
    return ["usr/bin/sccache-dist"]
