pkgname = "gn"
pkgver = "0_git20240402"
pkgrel = 0
_gitrev = "415b3b19e094cd4b6982147693485df65037f942"
hostmakedepends = ["ninja", "python"]
depends = ["ninja"]
pkgdesc = "Build system that generates ninja"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://gn.googlesource.com/gn"
# shamelessly leech off alpine
source = f"https://ab-sn.lnl.gay/gn-{_gitrev}.tar.zst"
sha256 = "47419d585f533f7b903d7dc85b66b88a72bc7f8bf788d9e2093a981acc7379a6"
hardening = ["vis", "cfi"]


def configure(self):
    self.do(
        "python",
        "./build/gen.py",
        "--no-last-commit-position",
        "--no-static-libstdc++",
        "--no-strip",
        "--allow-warnings",
    )


def build(self):
    self.do("ninja", f"-j{self.make_jobs}", "-C", "out")


def check(self):
    self.do("./out/gn_unittests")


def install(self):
    self.install_license("LICENSE")
    self.install_bin("out/gn")
