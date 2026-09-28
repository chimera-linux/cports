pkgname = "wasi-libc"
pkgver = "0.20250204"
pkgrel = 0
_gitrev = "e9524a0980b9bb6bb92e87a41ed1055bdda5bb86"
hostmakedepends = ["bash"]
pkgdesc = "WebAssembly libc implementation"
license = "Apache-2.0 WITH LLVM-exception AND Apache-2.0 AND MIT AND CC0-1.0 AND BSD-2-Clause"
url = "https://github.com/WebAssembly/wasi-libc"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "9bae87650be66d10662055ec138c6550b127f1ceedaf079266f89b7c7dfb7f34"
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
