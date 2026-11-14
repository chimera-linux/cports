pkgname = "tree-sitter-cli"
# match to tree-sitter
pkgver = "0.27.2"
pkgrel = 0
build_style = "cargo"
make_build_args = ["-p", "tree-sitter-cli"]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "cmake"]
makedepends = ["rust-std"]
pkgdesc = "Parser generator tool for tree-sitter bindings"
license = "MIT"
url = "https://tree-sitter.github.io/tree-sitter"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "356528363bf7fbad12a2cfeb5a2678c0118ef886a4d69ad9a379db5fdef0735f"
# requires fetching fixtures
options = ["!check"]

if self.profile.arch in ["aarch64", "x86_64"]:
    make_build_args += ["--features", "wasm"]
    make_check_args += ["--features", "wasm"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "tree-sitter"))
    self.install_license("LICENSE")
