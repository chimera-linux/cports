pkgname = "rust-bootstrap"
pkgver = "1.59.0"
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
    case "aarch64":
        sha256 = [
            "3c2ed1312f4f68c304389f83670f83ca85aca51374953d3b1af91f642ceaa7cf",
            "0b2359ef5971f5c5e07dc454b3e01360d90d26be066ef9990a22850494b364e2",
        ]
    case "ppc64le":
        sha256 = [
            "edb7581e9f3412a169be84aefd26817b98c25033e871dc68defdd60bdc0ed414",
            "92a1e3eb69204bda7a41ec74a6a56264607af098b64793d9a31cba0c159cd751",
        ]
    case "x86_64":
        sha256 = [
            "93730fe852e681d058e6169ec7c74ba1a5d58edbed092cc61c0752fbf7771f1f",
            "525b12f2603918d21018a7606e22e95f55380c3001c572c3718016d03e93f635",
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
