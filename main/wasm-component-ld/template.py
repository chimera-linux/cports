pkgname = "wasm-component-ld"
pkgver = "0.5.10"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["lld"]
checkdepends = ["rust-wasm", *depends]
pkgdesc = "Linker for webassembly components"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT"
url = "https://github.com/bytecodealliance/wasm-component-ld"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "aa049a93da595e4dacf742865f13e7fb1cec1ab47de9258f0a11d81ad6c7a77b"


def post_install(self):
    self.install_license("LICENSE-MIT")
