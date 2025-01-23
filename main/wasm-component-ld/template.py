pkgname = "wasm-component-ld"
pkgver = "0.5.12"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["lld"]
checkdepends = ["rust-wasm", *depends]
pkgdesc = "Linker for webassembly components"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT"
url = "https://github.com/bytecodealliance/wasm-component-ld"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d9747c922bdeda3490405d62669d3d74c4dc39481a10e5302db6deece768623a"


def post_install(self):
    self.install_license("LICENSE-MIT")
