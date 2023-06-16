pkgname = "rust-bootstrap"
pkgver = "1.70.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib", "ncurses-libs", "libzstd"]
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
            "6812139c5ef6fd0234565ecd74acc91fe59ddf70a44fb9a957fd2c50f9c03f69",
            "d6f0ab01a22e3905c795072df6a806b2d7b32f5ba57f944e73a6d193e276aa2d",
        ]
    case "ppc64le":
        sha256 = [
            "99b35e6d8d1b24b54945906554cf9b1b66994f684d29c7976108d33a694320d4",
            "3bd65fa65164ac67fffcddbe332488c2e40d31c9a2a887d60a01530c54e64dfb",
        ]
    case "ppc64":
        sha256 = [
            "6dc58254db3e9347e6ab5b729cc7cece3bb2407faa3a856087f7a30aef4b651e",
            "894cd5b0ac79df506b8fe690df1b320f57baa5c7ee7573104ad29b7cb16742e1",
        ]
    case "riscv64":
        sha256 = [
            "cef35245dd9219e7e34c322007ad577b4f205b19d0b04ed12c855eaf79c6bf1b",
            "c921123c5655d5ab80389f5c416d2efc487eab83be753f8b0f09f6aa3943a64b",
        ]
    case "x86_64":
        sha256 = [
            "ccf7e19e011789b5c22baed9e196c04f9b4c4f835670b0cfba438498a9404957",
            "2c4fdd53d942037f6286a22850146cf56ed898735a357c9fc6b5b2cf406b0c59",
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
