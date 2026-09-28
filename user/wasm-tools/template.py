pkgname = "wasm-tools"
pkgver = "1.229.0"
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
license = "Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT"
url = "https://github.com/bytecodealliance/wasm-tools"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ff3769834160b5bf1733daeeae14e6d74df85edcf49f300601927ef574790f9b"
# needs checked out submodules and whatever
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
