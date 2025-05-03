pkgname = "jaq"
pkgver = "2.2.0"
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
sha256 = "eee6a4d608c31c12c82644f1cdb69cfed55bb079806ec939e4de486bb252c631"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/jaq")
    self.install_license("LICENSE-MIT")
