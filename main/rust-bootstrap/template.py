pkgname = "rust-bootstrap"
pkgver = "1.82.0"
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
            "721aae834d1e28b904ef4ef47daf4a4c801f587a4c4b878e7cc5cfbd7ba76123",
            "a65340817dcd7ab338bd734bbfb8c512d64f7f6c38c2e4a195340e65b6f7c26b",
        ]
    case "ppc64le":
        sha256 = [
            "b3b88c68b7a95ea534cb3aaa76d8b8e9c5462a9749bda7ff342b984f8940461c",
            "a827a01b5cb81cfbb5e1a7fb9dff5f4fc6d6f8d01b3ad29f38f90d5ede05a918",
        ]
    case "ppc64":
        sha256 = [
            "e638ffa056492a89b575596ca83441c7c69e1af6ac023e3ef73f22f2b874be34",
            "bb08f0ce30e33c92036fc09695c6dcfadccf470e5846d0db1aa0d2893ee8d73a",
        ]
    case "riscv64":
        sha256 = [
            "82c8de56283ee520734e104a6aebcd7034c9009bd47709d39d18f2e8805c5d3d",
            "c776824d41f74d92fca824c9000c72287cd42252c6f60b9ac983cde0318c5781",
        ]
    case "x86_64":
        sha256 = [
            "85e8357944e6112d2c77554c3c0e09e1517266b5543050e35abc276fd44f7b5a",
            "1a484e63937eaf9023181542618df9390a60de9f56b80e2b76c3317b6e3e9086",
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
