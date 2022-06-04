pkgname = "rust-bootstrap"
pkgver = "1.61.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib", "ncurses-libs"]
# overlapping files
depends = ["!rust"]
pkgdesc = "Rust programming language bootstrap toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
_urlb = "https://ftp.octaforge.org/chimera/distfiles"
source = [
    f"{_urlb}/rustc-{pkgver}-{self.profile().triplet}.tar.xz",
    f"{_urlb}/rust-std-{pkgver}-{self.profile().triplet}.tar.xz"
]
options = ["!strip"]

match self.profile().arch:
    case "ppc64le":
        sha256 = [
            "1f334527f4067729e8e4f5605507269d3b9638d86a9e5d6ab96d02c3bd3592aa",
            "0aed1fa0d893baad2ea46fc4cfc875166e1edb4e227b5c2bc290d680114efbbf",
        ]
    case "x86_64":
        sha256 = [
            "48a8475d2436815b320ffe336f6805ad2f5f2424ac571f1491d1080ce749d5cc",
            "78353b58110a64b4ceb55a08c233bca2fb0eab717a6f281b9e9e768d2119908a",
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
