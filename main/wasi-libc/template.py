pkgname = "wasi-libc"
pkgver = "0.20240103"
pkgrel = 0
_gitrev = "925ad6d75899397d26b9f09a6f195dbf5eb35814"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "WebAssembly libc implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception AND Apache-2.0 AND MIT AND CC0-1.0 AND BSD-2-Clause"
url = "https://github.com/WebAssembly/wasi-libc"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "236fa7fc985a69e7dbbbbf5074c703d81e1388c531e2ff484587287462618d95"
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
