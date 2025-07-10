pkgname = "jaq"
pkgver = "2.3.0"
pkgrel = 0
build_style = "cargo"
# disable the default mimalloc feature and just use the system allocator
make_build_args = ["--no-default-features", "--bin", "jaq"]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "JSON data processing tool with jq compatible syntax"
license = "MIT"
url = "https://github.com/01mf02/jaq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "80fae7c5bbbc244580ca77d3e5a4fc6e9c3ea08a5526d562e3c5300edd44fe8b"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/jaq")
    self.install_license("LICENSE-MIT")
