pkgname = "wasm-component-ld"
pkgver = "0.5.5"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
depends = ["lld"]
checkdepends = ["rust-wasm", *depends]
pkgdesc = "Linker for webassembly components"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT"
url = "https://github.com/bytecodealliance/wasm-component-ld"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e604fd428e039c44f47735892c6a22c1e7f5dea98d31ea77cd1ab36a42cc87f9"


def post_install(self):
    self.install_license("LICENSE-MIT")
