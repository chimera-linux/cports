pkgname = "frawk"
pkgver = "0.4.7"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "cargo"
# disable llvm_backend (needs LLVM 12), unstable and use-jemalloc features
make_build_args = ["--no-default-features", "--features=allow_avx2"]
make_install_args = list(make_build_args)
make_check_args = list(make_build_args)
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "Awk-like language"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "MIT OR Apache-2.0"
url = "https://github.com/ezrosent/frawk"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7ec5d93f3a9ee3c4bafc7db790ea471a568e94de657fbb74d7a3b641bf3e68e6"


def do_prepare(self):
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("LICENSE-MIT")
