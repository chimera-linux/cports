pkgname = "tree-sitter-cli"
# match to tree-sitter
pkgver = "0.22.6"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "tree-sitter-cli"]
make_check_args = list(make_build_args)
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Parser generator tool for tree-sitter bindings"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://tree-sitter.github.io/tree-sitter"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "e2b687f74358ab6404730b7fb1a1ced7ddb3780202d37595ecd7b20a8f41861f"
# requires fetching fixtures
options = ["!check"]

if self.profile().arch in ["aarch64", "x86_64"]:
    make_build_args += ["--features", "wasm"]
    make_check_args += ["--features", "wasm"]


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/tree-sitter")
    self.install_license("LICENSE")
