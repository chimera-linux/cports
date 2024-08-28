pkgname = "rust-bootstrap"
pkgver = "1.79.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib-ng-compat", "ncurses-libs", "zstd"]
# overlapping files
depends = ["!rust"]
pkgdesc = "Rust programming language bootstrap toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
_urlb = "https://repo.chimera-linux.org/distfiles"
source = [
    f"{_urlb}/rustc-{pkgver}-{self.profile().triplet}.tar.xz",
    f"{_urlb}/rust-std-{pkgver}-{self.profile().triplet}.tar.xz",
]
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = [
            "b8d0f7d180ea6b1691f9730352b1c06ab3f5e4d01d68c1dad854b434a8dcdbc5",
            "ceb9a1de0640948e548163eade23c234498a8c206041bcfe179adcc36e762b9d",
        ]
    case "ppc64le":
        sha256 = [
            "53f88c90b29a489bff11dd06f3a6bb28018757e17bc069bcb5d571c6b44381dc",
            "d8a3fdff05f02c4509b2d1839e8e0f66ff2f7b8ae5fecb59d9270c5486a52430",
        ]
    case "ppc64":
        sha256 = [
            "3883ce773a8f01478433690cd3c84cda2c5cb44687b045ad96c98e214457a7f3",
            "ca515134c00dd835691f2d5513d06bf43a375ca2f0348a2f3e55e1d620a75c75",
        ]
    case "riscv64":
        sha256 = [
            "2c1b8833513a7943e32d2962b5f62de39685fc14ecff2c700cdb8ee6f8c1e8d3",
            "7c3f83c614dc1a0dd3cc98c03dba5231c619f53fde0c384d6bbc0cb1438ed251",
        ]
    case "x86_64":
        sha256 = [
            "258b42c9c26177852196156d88832953b7dffc37d3cbe97c901c1d66ea1a304a",
            "8bf777bb16f054b6d9dcaf61b3cd2f57c9ffc3deb0a4ec0162e1de87ad6d198e",
        ]
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    for d in self.cwd.iterdir():
        self.do(
            self.chroot_cwd / d.name / "install.sh",
            "--prefix=/usr",
            f"--destdir={self.chroot_destdir}",
            wrksrc=d.name,
        )
    # remove rust copies of llvm tools
    trip = self.profile().triplet
    for f in (self.destdir / f"usr/lib/rustlib/{trip}/bin").glob("rust-ll*"):
        f.unlink()
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
