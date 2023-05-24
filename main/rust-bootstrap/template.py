pkgname = "rust-bootstrap"
pkgver = "1.69.0"
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
    f"{_urlb}/rust-std-{pkgver}-{self.profile().triplet}.tar.xz",
]
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = [
            "da859adf3961b7961945cbb89fb9da5dc7db459d345bdc83cf4630c6e1f479fa",
            "7c43ff307cedd873bce191606500b917b262e5cf0569a99075ae26b92701cf37",
        ]
    case "ppc64le":
        sha256 = [
            "52867a8302e2b4e0efc5b37f5dbdec7feb31dfb3fc8255a5cce5fe798726c603",
            "24f4d55809e84cfe7e1c0fc8168c1d9a4008aef3ed662dc931f3724abd80c242",
        ]
    case "riscv64":
        sha256 = [
            "c39d4d175abcfb12f4e7031fb7bfe2f28dfea136343294fd663cb5eb2d199bf1",
            "5921299e9959fe22634e06fed2ab9420cc939c5a7ab6651149d14e7982874616",
        ]
    case "x86_64":
        sha256 = [
            "a44f69f77aa2b6be3d352d3e44c8969bc11ab8b7d284abf97de8a6191bb17a4c",
            "055c673a73240e3d4c8331c36f8cb563b2e8e583deb8d089c35e619a58e8e844",
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
