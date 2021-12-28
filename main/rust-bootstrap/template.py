pkgname = "rust-bootstrap"
pkgver = "1.57.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib", "ncurses-libs"]
# overlapping files
depends = ["!rust"]
# cargo-bootstrap can depend on this
provides = [f"rust-bootstrap-virtual={pkgver}-r{pkgrel}"]
provider_priority = 0
pkgdesc = "Rust programming language bootstrap toolchain"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
_urlb = "https://ftp.octaforge.org/q66/random/rust-chimera"
source = [
    f"{_urlb}/rustc-{pkgver}-{self.profile().triplet}.tar.xz",
    f"{_urlb}/rust-std-{pkgver}-{self.profile().triplet}.tar.xz"
]
options = ["!strip"]

match self.profile().arch:
    case "aarch64":
        sha256 = [
            "c9382d56949eb427648850b8595ac39b4542822b5b4b223a067a202fb57f6968",
            "4e11271df34353e139f18e05573b75be4be80bd14c8315edfa271c61ea25ec42",
        ]
    case "ppc64le":
        sha256 = [
            "f4960ca2bcc9f147b2e8f45e4e9d65ab1bd40979f3f3ff4914b52597c526546d",
            "618c5a93f37ec8c2a5e10e57fb5d259e17aa2acef3ede9426cfebbb5eb5022a7",
        ]
    case "x86_64":
        sha256 = [
            "0add5ffc9271925ed470aa3de6c7fea39dbf4e7d2f6be55b410c69297bd0ec09",
            "0177e357ee80541c8abd737fdf0af15c7df7d06f8758de8f6fb0af3a884a4a8b",
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
