pkgname = "gn"
pkgver = "0_git20261020"
pkgrel = 0
_gitrev = "938087829fcbcc8fd87835ee301dd522c7637685"
hostmakedepends = ["ninja", "python"]
depends = ["ninja"]
pkgdesc = "Build system that generates ninja"
license = "BSD-3-Clause"
url = "https://gn.googlesource.com/gn"
source = f"https://ftp.octaforge.org/q66/random/gn-{_gitrev}.tar.gz"
sha256 = "0b96819efc688acfd1e61665fe8f56e60d08fb3db144140d8f6124e034edd552"
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
