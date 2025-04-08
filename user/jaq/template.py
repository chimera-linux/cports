pkgname = "jaq"
pkgver = "2.1.1"
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
sha256 = "b8276f6618bd69b2d8feb8d76b927a6debe1bc950742d344643cc4e4d0849009"


def install(self):
    self.cargo.install(wrksrc="jaq")
    self.install_license("LICENSE-MIT")
