pkgname = "rust-bootstrap"
pkgver = "1.64.0"
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
            "0ee65bb45e1688a1b7b44f418b2f209bb99722ff4cd7ae7b73526d914b4f5be5",
            "41c6c3d9eed7b3b6c63796b8dcaecc9516a2970fc61644b3d3cb35275c9ac04c",
        ]
    case "ppc64le":
        sha256 = [
            "b10c3531937b1bd7be66ce1f1afcd7d96c5476321f12a7fe906cfd0f718fdd18",
            "ef5063ea486034be5a977e88bf7172d99e7e1832ca978022f18b46238dd626fd",
        ]
    case "x86_64":
        sha256 = [
            "a65afc2029b6feb3262b7354c50d936e545c0e15accce00869495aeeeb676e77",
            "e5fe55926a716ba90a5c25e116ee7250962d4fa4849c1f1e077bbefd54ea5ca4",
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
