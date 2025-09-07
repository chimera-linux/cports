pkgname = "hashcat"
pkgver = "7.1.2"
pkgrel = 0
build_style = "makefile"
make_env = {
    "PREFIX": "/usr",
    "SED": "/usr/bin/gsed",
    "USE_SYSTEM_OPENCL": "1",
    "USE_SYSTEM_XXHASH": "1",
    "USE_SYSTEM_ZLIB": "1",
    # prevents -march=native from being passed
    "MAINTAINER_MODE": "1",
}
make_use_env = True
hostmakedepends = [
    "cargo",
    "gsed",
]
makedepends = [
    "linux-headers",
    "minizip-devel",
    "opencl-headers",
    "python-devel",
    "rust-std",
    "xxhash-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Password recovery tool"
license = "MIT"
url = "https://hashcat.net/hashcat"
source = f"https://hashcat.net/files/hashcat-{pkgver}.tar.gz"
sha256 = "9546a6326d747530b44fcc079babad40304a87f32d3c9080016d58b39cfc8b96"
# check: no obvious test suite
options = ["!check", "!cross"]


if self.profile().endian == "big":
    broken = "bug endian"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(
        ["--manifest-path", "Rust/generic_hash/Cargo.toml"]
    )


def init_build(self):
    from cbuild.util import cargo

    self.make_env.update(cargo.get_environment(self))


def post_install(self):
    self.install_license("docs/license.txt")
