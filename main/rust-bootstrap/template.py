pkgname = "rust-bootstrap"
pkgver = "1.67.0"
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
            "b28df0b866452d92c2b4e0473c4b14485b6135450a5a40ff8d20b59f38a73f2e",
            "466aa4f5d04f829ad876a01d1a864f75f668bce6f55f3c1321951a3e655f1906",
        ]
    case "ppc64le":
        sha256 = [
            "7cf7dda7b6a0a7c5c3360a778489257e7e8f0914feb8bd8763f8171dffaa9d9a",
            "2d7f80a60b9f3a399ba708782019ba2bd3df8e98ea3c846ce57dee172364d432",
        ]
    case "riscv64":
        sha256 = [
            "eb7cbf08fdcf5d097983f4449b0f86bd59e503cee2e21cf21a9cb11ee2e8dab1",
            "35c304e7ba96b8245050ae40b8799d747e30f40c87108004078e71ee4c658006",
        ]
    case "x86_64":
        sha256 = [
            "610a6df0d9f23e0cd1fc9cfcdb67479d8518d422527255205c9699240ba8339e",
            "d010e4bd8c9acc568391ad89e43e14a863ce4a550ff600a96b34f95f6b365adf",
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
