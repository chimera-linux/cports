pkgname = "rust-bootstrap"
pkgver = "1.80.1"
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
            "9c6bc7694ea05265105d7090347de2f28ffd616fbd46ce460bc2b02e15986ea8",
            "11dba676a90daef2e899803074f8b924205dd13dfe7161935ec8e1feb5d06efb",
        ]
    case "ppc64le":
        sha256 = [
            "5c91c3c5998bb79ff27eb59aaebea95ed27ee5bb3eaf9ad96e1f4d7ab2723759",
            "a1d6eec7c89b34b24b1a811268f16f85aee75ce230d66a6b504de0688a1bdf79",
        ]
    case "ppc64":
        sha256 = [
            "2375a3a53aadc60b1249ae9e732a2141dd5bfb71bfc4423ae21ada2a60bf2063",
            "35a004a2e69a4d0e93fda746d4c124fef2469107c801eb28a9ad1751d00e753e",
        ]
    case "riscv64":
        sha256 = [
            "dd52a691e8d8c729b8dccf1beece71cd6e5c55b96ca15987a07c3c6bd92b4233",
            "f2f8fa7572508123614657cb46df06ec4d7d5aa55bebd762a613eaa865920143",
        ]
    case "x86_64":
        sha256 = [
            "56a376693bf5eac016da9c33f7e9dd4297724d3cf0a6d7aa95795798ff654f7a",
            "09c770042643e5501c3584549d9690217f58e884f826a1e9be6226e5947117ea",
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
