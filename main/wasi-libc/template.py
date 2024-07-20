pkgname = "wasi-libc"
pkgver = "0.20240708"
pkgrel = 0
_gitrev = "3f43ea9abb24ed8d24d760989e1d87ea385f8eaa"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "WebAssembly libc implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception AND Apache-2.0 AND MIT AND CC0-1.0 AND BSD-2-Clause"
url = "https://github.com/WebAssembly/wasi-libc"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "8c02329d63e23a8aa7187e83f70daa2eed69cdc84ebcc753201c2caf4fb1b207"
# no tests
options = ["!check", "!lto"]

_targets = [
    ("wasm32-wasip1", ""),
    ("wasm32-wasip1-threads", "THREAD_MODEL=posix"),
    ("wasm32-wasip2", "WASI_SNAPSHOT=p2"),
]


def do_build(self):
    for tgt in _targets:
        self.do(
            "gmake",
            f"-j{self.make_jobs}",
            "CC=clang",
            f"TARGET_TRIPLE={tgt[0]}",
            tgt[1],
        )


def do_install(self):
    self.do(
        "gmake",
        "install",
        f"INSTALL_DIR={self.chroot_destdir / 'usr/wasm32-unknown-wasi'}",
    )
    self.install_license("LICENSE")
    self.install_license("LICENSE-MIT")
