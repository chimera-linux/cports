pkgname = "rust-bootstrap"
pkgver = "1.65.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib", "ncurses-libs"]
# overlapping files
depends = ["!rust"]
pkgdesc = "Rust programming language bootstrap toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
_urlb = "https://repo.chimera-linux.org/distfiles"
source = [
    f"{_urlb}/rustc-{pkgver}-{self.profile().triplet}.tar.xz",
    f"{_urlb}/rust-std-{pkgver}-{self.profile().triplet}.tar.xz"
]
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = [
            "d87e536e5ac8cc80a52617a96ff846724eac29ae11de4b383d63fadef91b937f",
            "ca6b917ca8f3453a681b0ba04338a73e48f002db0ffdfa0b4ad06b3c28645aca",
        ]
    case "ppc64le":
        sha256 = [
            "9bf0791a960a6455602d12ac14b7d0febb0eccd8d0af467a185232de33fa3469",
            "2ee37a9bfb06dc8637b56c9e2d0af6dd6193a7191fa0c43459d227d91a879037",
        ]
    case "riscv64":
        sha256 = [
            "47cf0d3770defd01bdc2ebae64992d5a9d805b04965c7314cf615ffa86d3eb06",
            "751897bc5a1748eddf37dde2af002633eca6d5bf174c460ff32b43fd7ec28d5e",
        ]
    case "x86_64":
        sha256 = [
            "0d8844c0c597534341e6cc3b9d5cd804a6fdf39a8b6eca9aa75cad5c5ab73207",
            "2f5335e1ea674c39304a942ce8f6898278f86aa860426be09da3aa37b9834927",
        ]
    case _:
        broken = f"not yet built for {self.profile().arch}"

def do_install(self):
    for d in self.cwd.iterdir():
        self.do(
            self.chroot_cwd / d.name / "install.sh", "--prefix=/usr",
            f"--destdir={self.chroot_destdir}",
            wrksrc = d.name
        )
    # remove rust copies of llvm tools
    trip = self.profile().triplet
    for f in (self.destdir / f"usr/lib/rustlib/{trip}/bin").glob("rust-ll*"):
        f.unlink()
