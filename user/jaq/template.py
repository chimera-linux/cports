pkgname = "jaq"
pkgver = "2.0.1"
pkgrel = 1
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
sha256 = "e554f375500d09813c9a2f4454217b8d12ae3be5dba56bc545b199ae0d4ab72e"


def install(self):
    self.cargo.install(wrksrc="jaq")
    self.install_license("LICENSE-MIT")
