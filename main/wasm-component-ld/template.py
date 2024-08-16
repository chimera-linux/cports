pkgname = "wasm-component-ld"
pkgver = "0.5.6"
pkgrel = 1
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
sha256 = "9bb1d09d315a3412c2cb0d5533c03490bf9d96af709ee93a4901137f5292265a"


def post_install(self):
    self.install_license("LICENSE-MIT")
