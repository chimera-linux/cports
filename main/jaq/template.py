pkgname = "jaq"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cargo"
# disable the default mimalloc feature and just use the system allocator
make_build_args = ["--no-default-features", "--bin", "jaq"]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "JSON data processing tool with jq compatible syntax"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/01mf02/jaq"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "7535387562c0e5519811bfd1f405eb8cb7683533781e0790981221e8e5b723c2"


def install(self):
    self.cargo.install(wrksrc="jaq")
    self.install_license("LICENSE-MIT")
