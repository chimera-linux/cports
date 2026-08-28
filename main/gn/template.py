pkgname = "gn"
pkgver = "0_git20260605"
pkgrel = 0
_gitrev = "c1b663788ed1ecf2ffd53781c98ae2291ee002cf"
hostmakedepends = ["ninja", "python"]
depends = ["ninja"]
pkgdesc = "Build system that generates ninja"
license = "BSD-3-Clause"
url = "https://gn.googlesource.com/gn"
source = f"https://ftp.octaforge.org/q66/random/gn-{_gitrev}.tar.gz"
sha256 = "3882057b70f010ef1501f12f04af6c567499b77be2a402ffffc7c6edc3393e8d"
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
