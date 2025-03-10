pkgname = "gn"
pkgver = "0_git20250113"
pkgrel = 0
_gitrev = "ed1abc107815210dc66ec439542bee2f6cbabc00"
hostmakedepends = ["ninja", "python"]
depends = ["ninja"]
pkgdesc = "Build system that generates ninja"
license = "BSD-3-Clause"
url = "https://gn.googlesource.com/gn"
# shamelessly leech off alpine
source = f"https://ab-sn.lnl.gay/gn-{_gitrev}.tar.zst"
sha256 = "1d092838aea0fbb184b0398bfabd07d894b8a03ddf543b81fb3fd238f43d205d"
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
