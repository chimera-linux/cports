pkgname = "wasm-component-ld"
pkgver = "0.5.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
depends = ["lld"]
checkdepends = ["rust-wasm"] + depends
pkgdesc = "Linker for webassembly components"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT"
url = "https://github.com/bytecodealliance/wasm-component-ld"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "78483e8bf35aabe0ccdedd2a2fe61a382038bb883b3389c1686fedac3f32a5db"


def post_install(self):
    self.install_license("LICENSE-MIT")
