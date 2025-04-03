pkgname = "gn"
pkgver = "0_git20250324"
pkgrel = 0
_gitrev = "6e8e0d6d4a151ab2ed9b4a35366e630c55888444"
hostmakedepends = ["ninja", "python"]
depends = ["ninja"]
pkgdesc = "Build system that generates ninja"
license = "BSD-3-Clause"
url = "https://gn.googlesource.com/gn"
source = f"https://ftp.octaforge.org/q66/random/gn-{_gitrev}.tar.gz"
sha256 = "d5d3d6b928853a1cedeeca6c023496b3172413822aba3a0148313f29e23bbc97"
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
