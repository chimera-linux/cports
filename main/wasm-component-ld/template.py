pkgname = "wasm-component-ld"
pkgver = "0.5.7"
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
sha256 = "f046d4eb152bbb5637fede88c8f3afacdb64f94ce61448d3ccb71a7b652816ef"


def post_install(self):
    self.install_license("LICENSE-MIT")
