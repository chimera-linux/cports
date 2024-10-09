pkgname = "wasm-tools"
pkgver = "1.219.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT"
url = "https://github.com/bytecodealliance/wasm-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6d127c70c56d873b3e99570fb6cdc76f5877688abf94f6e2dea905c5291ab751"
# needs checked out submodules and whatever
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
