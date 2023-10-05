pkgname = "rust-bootstrap"
pkgver = "1.72.0"
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
            "d898a9a63ef6ccc8d4ab796429f2159e0ee34c3a8a03fbb8c37edd8b166631ab",
            "9d235a499ecf7247950bf15f8c2abb4323a1153adef24350453fca7a1740e22c",
        ]
    case "ppc64le":
        sha256 = [
            "1b3c328e68005d6d55152de931f8679a25b4db14fb265d732ea2af3d99927c77",
            "4667147b9f93d662952048ff97e488e33d99f8aff996dff6f993f0c2f48d2c98",
        ]
    case "ppc64":
        sha256 = [
            "673fd30490da2496c5fef2ab21986a2d452185606b57ef0ee1aa24a89b026679",
            "3f2acf1802b6d79c0b5e3af99abe97480a6d595b3014c68f39fde4c915187856",
        ]
    case "riscv64":
        sha256 = [
            "9aabd5168c5ef991e466b1b3cf0e8a527d29c4dcf94ee046ce22bd2199834b86",
            "d16939379e523332b10912d9537903401752478f5634613bc1830a2c471916b3",
        ]
    case "x86_64":
        sha256 = [
            "d25ae1bd2d9754d305232d9003199094e6cf0b03bb6fd9b0745515c63ca90eab",
            "636c6b06951bf6ba6762d6ee311e45a0c62b6a4736ffaa99c1f70d97d1bdfa93",
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
