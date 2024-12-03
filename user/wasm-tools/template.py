pkgname = "wasm-tools"
pkgver = "1.221.2"
pkgrel = 0
# wasmtime
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "cargo"
hostmakedepends = [
    # cargo-auditable broken for some reason
    "cargo",
]
makedepends = ["rust-std"]
pkgdesc = "CLI for manipulation of wasm modules"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT"
url = "https://github.com/bytecodealliance/wasm-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9940c19aa878f500a031282f13401fb6177517a238220246bbcea0d642ee8934"
# needs checked out submodules and whatever
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
