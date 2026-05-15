pkgname = "gn"
pkgver = "0_git20260502"
pkgrel = 0
_gitrev = "8dc9a7962b016e02df152e53a231876fcc515259"
hostmakedepends = ["ninja", "python"]
depends = ["ninja"]
pkgdesc = "Build system that generates ninja"
license = "BSD-3-Clause"
url = "https://gn.googlesource.com/gn"
source = f"https://ftp.octaforge.org/q66/random/gn-{_gitrev}.tar.gz"
sha256 = "10a94ee19fcf892b0f60ea7f51ccab401312b1c6547d39a9f3fb6d0315aefd5e"
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
