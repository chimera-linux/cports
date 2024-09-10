pkgname = "wasm-component-ld"
pkgver = "0.5.8"
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
sha256 = "b1cb7ecfab5548d71d3c5dc4b96da03a1a544eb7c56cb3155f89dba2bdfb244e"


def post_install(self):
    self.install_license("LICENSE-MIT")
