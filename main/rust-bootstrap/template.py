pkgname = "rust-bootstrap"
pkgver = "1.73.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib", "ncurses-libs", "zstd"]
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
            "4f1b557f0baeff663024e896303c7e570afbbced3c72d6f71ef59f7459691714",
            "f85ceb999efcadc52a019aa13bd1a0dc6b68bfd48803b86a888305733071314a",
        ]
    case "ppc64le":
        sha256 = [
            "4bf17cf8794102b99221a173225132a2c9c81e1149e4b3caa8484f1c6394899c",
            "81c71f7bcef19b1cb5688882e8450379cfe334d89df2355a13e111397082a6a8",
        ]
    case "ppc64":
        sha256 = [
            "68b115d85f52f6243f27943167df8cda69a63a8312bb59fd8de4918921913a4f",
            "214fe38264928cc7cb9b8c5397a25b2e6d3ff66bb502495e4e8195510fab84a4",
        ]
    case "riscv64":
        sha256 = [
            "3a9662524eb5e91393c4a1f30e3f29258a5ef34e85d22e25f1c785ec36eb605f",
            "063955168a6c1f2fcf0d305953a0dd639f0b0f989bdae6848128f87fee0a3668",
        ]
    case "x86_64":
        sha256 = [
            "b15cf90e2668815c0bdd63204eb8ff8071679b4afcc8cec39917cc2d363125be",
            "dbabb1af291ac833e19ac632a4edc78b4d07235bc4fdad4c2fc96f081e944df7",
        ]
    case _:
        broken = f"not yet built for {self.profile().arch}"


def do_install(self):
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
