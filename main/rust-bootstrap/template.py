pkgname = "rust-bootstrap"
pkgver = "1.74.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib", "ncurses-libs", "zstd"]
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
            "a0c5ad9ebf87e0999bb741d801020c5afc685ae685b7a7ab71754eabf656ce59",
            "fbe43d939727c227902fcf61b8f93e78118bc986e8c175dae6b711198f51e23c",
        ]
    case "ppc64le":
        sha256 = [
            "65a0ec426ef429b85b611a42916ed1c5be69cef4e10c3ad64b5ebfe1e6782df1",
            "ddab3e32421053899bb1b3f08272e454bf8f615f340c3b04ed9ee3c7b492ecba",
        ]
    case "ppc64":
        sha256 = [
            "19f94672efe7155314d7a8899f28343a59610cfa3e64c2cd1d32d7f0bd339bcf",
            "e6ea813e9bf17e6d1fdb04b05fec996740d473c7ab3d26ffdd1adb2347ad54ad",
        ]
    case "riscv64":
        sha256 = [
            "2b5a067c7df45a2936d3c830f4fd181d2f4abdb54422cb39447af59acbef81b4",
            "501de9a5e1dd8f07ac371bf1ff7704bad886fc1a6dcde18dd142e69e284b1f6c",
        ]
    case "x86_64":
        sha256 = [
            "a6839391661f25a6842c74707338ef7ebc8edef8a7cef7c2e3ebca582650911d",
            "53d75bfb9f5ac99e0ac15d6334bd6c06748914f7eeb5978555bc24b93cf84eb8",
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
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
