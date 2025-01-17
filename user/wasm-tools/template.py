pkgname = "wasm-tools"
pkgver = "1.223.0"
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
sha256 = "bded9fb68df0fa14f80a37609c272c20a9f35b20c897b9900305ccaa3f93d6d2"
# needs checked out submodules and whatever
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
