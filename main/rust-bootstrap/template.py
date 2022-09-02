pkgname = "rust-bootstrap"
pkgver = "1.63.0"
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
            "96bc34cbb405b06918255c03e1aef3cf68308156747364012477bb783860213f",
            "f9fb9d0ad89237e8371e3e6d4a1ea0583461ebe8ef97800c2971f7e609ff7606",
        ]
    case "ppc64le":
        sha256 = [
            "586ef746994b1c6a9b737abca23da42b021106c402cf6b0c2f0711c076f3ec1a",
            "7310677edeae15a0a896f137c80a54a1faf4f196ad60de1539fbac3e1b6f901c",
        ]
    case "x86_64":
        sha256 = [
            "0d110cded4380203b48c641ea651af1e895b6758a6af22a6f43445984a545fba",
            "14a12273b018b9cbe07b73699689f773f795e72ba9ffddff2a5881128eb94676",
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
