pkgname = "rust-bootstrap"
pkgver = "1.60.0"
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
            "b23bc823f0208049554df1f526c740684f36a6e33d79977114b361e6cb5fd244",
            "3a4644b7487732b581bff1da539f64f99f25ec2b6b85d2f7183333faea167999",
        ]
    case "x86_64":
        sha256 = [
            "990f6bdb44956444cc8a280be41f59bf3147775f08cbc69bf2fbbf40a0a90178",
            "1bf6b7bf3eb2e2b0aec2e39e36a2db383bf05e6d095455d4fdfd33d1044a8e38",
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
