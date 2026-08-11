pkgname = "rust-bootstrap"
pkgver = "1.96.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib-ng-compat", "ncurses-libs", "zstd"]
# overlapping files
depends = ["!rust"]
pkgdesc = "Rust programming language bootstrap toolchain"
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
            "b7b92d0880d991d57985e4ef560e91d956d8b0de7062220f330d7fcb1a0ccef6",
            "a7f522959f2149011fcb4c881ff2d03ae9be10f7cee4f92037ab6fb0536ce57b",
        ]
    case "loongarch64":
        sha256 = [
            "eeeb1f448b82e6b81ce01cf59cfcc6a71f686263396bb734577a06183e34107d",
            "5ca9168628b6b7378278e0a149922e53b0e5f0215915e4b1a84d22facfd2ae00",
        ]
    case "ppc64le":
        sha256 = [
            "77f9e96d6ece90e2bb4f9c3f9b55987a9007b8d471344e03be3a971f0db01e4a",
            "48f0ff80cf6031e1e2b2bbff219c3121d061de133892c9379fa1e2a5acf2ff2f",
        ]
    case "riscv64":
        sha256 = [
            "61095e8eeb87f944f2250fa58fbea7df4bf025b94151e83909cef7cbef4169d6",
            "95a93829528e80ab35877d59f994a31341b6e7e5d4508c7422ba35707d1e9189",
        ]
    case "x86_64":
        sha256 = [
            "a938c5c95c6d305089e3cfa85724c1cdd5e8d2dd30aed61da288a144b9afc274",
            "74745320b617fa592720e8f00f5aded066e36be4689711d495bd7c0e4793f33d",
        ]
    case _:
        broken = f"not yet built for {self.profile().arch}"


def install(self):
    for d in self.cwd.iterdir():
        self.do(
            self.chroot_cwd / d.name / "install.sh",
            "--prefix=/usr",
            f"--destdir={self.chroot_destdir}",
            wrksrc=d.name,
        )
    # remove rust copies of llvm tools
    trip = self.profile().triplet
    self.uninstall(f"usr/lib/rustlib/{trip}/bin")
    # whatever
    self.uninstall("usr/etc")
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
