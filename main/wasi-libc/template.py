pkgname = "wasi-libc"
pkgver = "0.20240724"
pkgrel = 0
_gitrev = "b9ef79d7dbd47c6c5bafdae760823467c2f60b70"
pkgdesc = "WebAssembly libc implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception AND Apache-2.0 AND MIT AND CC0-1.0 AND BSD-2-Clause"
url = "https://github.com/WebAssembly/wasi-libc"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "9f557e81f7622cbf51b59eaf2d2ebceaa74eb745c4e557dbb5a01e9a36142040"
# no tests
options = ["!check", "!lto"]

_targets = [
    ("wasm32-wasip1", ""),
    ("wasm32-wasip1-threads", "THREAD_MODEL=posix"),
    ("wasm32-wasip2", "WASI_SNAPSHOT=p2"),
]


def build(self):
    for tgt in _targets:
        self.do(
            "make",
            f"-j{self.make_jobs}",
            "CC=clang",
            f"TARGET_TRIPLE={tgt[0]}",
            tgt[1],
        )


def install(self):
    self.do(
        "make",
        "install",
        f"INSTALL_DIR={self.chroot_destdir / 'usr/wasm32-unknown-wasi'}",
    )
    self.install_license("LICENSE")
    self.install_license("LICENSE-MIT")
