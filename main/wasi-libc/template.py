pkgname = "wasi-libc"
pkgver = "0.20240412"
pkgrel = 0
_gitrev = "9e8c542319242a5e536e14e6046de5968d298038"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "WebAssembly libc implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception AND Apache-2.0 AND MIT AND CC0-1.0 AND BSD-2-Clause"
url = "https://github.com/WebAssembly/wasi-libc"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "d86d115be80cc796da0e1b7d63f192da91e17927cf24273be7d89b2a9284ad4c"
# no tests
options = ["!check", "!lto"]


def do_build(self):
    # https://bugzilla.mozilla.org/show_bug.cgi?id=1773200#c4
    self.do("gmake", f"-j{self.make_jobs}", "CC=clang", "BULK_MEMORY_SOURCES=")
    self.do("gmake", f"-j{self.make_jobs}", "CC=clang", "THREAD_MODEL=posix")


def do_install(self):
    self.do(
        "gmake",
        "install",
        f"INSTALL_DIR={self.chroot_destdir / 'usr/wasm32-unknown-wasi'}",
    )
    self.install_license("LICENSE")
    self.install_license("LICENSE-MIT")
