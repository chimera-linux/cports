pkgname = "rust-bootstrap"
pkgver = "1.68.0"
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
            "bb5b6c0ec01906c1217b02dfe45fe9b39cf45104a53de0de5bc47d092d4034e1",
            "0bd0d4ce5f1413060207ef76b5c255520b9887c00cde3ae8d5c92a80166344ad",
        ]
    case "ppc64le":
        sha256 = [
            "59a39cc5ecae69c995346dc04bb6e03ac770299fba873870ead705f7fcdd1051",
            "10cda47222eb1aa865feac7a3d8bbc5227a730075b2dd820a5ee611d9596f4ad",
        ]
    case "riscv64":
        sha256 = [
            "1a6864b42d5178a40f15b71c7d233312b328699e7e26aefd4c0c6228f1bc99f4",
            "6549ec1fd47ae22acfab637c1fda6286c39180ee5fe84bb0b7aa3e81fe946379",
        ]
    case "x86_64":
        sha256 = [
            "374af4f128be70a4468df1faa765f6bdda10f9e066655d6f87985e11e6fa991b",
            "e4817030c3d7f13e82154f83e335bcf3363a9085db95d3354f2eb614e47f1058",
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
