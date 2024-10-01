pkgname = "binsider"
pkgver = "0.2.0"
pkgrel = 0
# inline asm for ppc64* needs nightly
# ppc64*/riscv64/aarch64 needs a new nix crate release for ptrace::getregs
archs = ["x86_64"]
build_style = "cargo"
make_check_args = ["--lib"]
hostmakedepends = ["cargo-auditable"]
depends = ["rust-std"]
pkgdesc = "TUI for analyzing ELF files"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "Apache-2.0 OR MIT"
url = "https://binsider.dev"
source = f"https://github.com/orhun/binsider/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f6792950c77795485414a4e82fce7898debed271a4d6fc6e509dc9bfe7879e72"


def post_install(self):
    self.install_license("LICENSE-MIT")
