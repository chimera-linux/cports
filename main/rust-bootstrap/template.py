pkgname = "rust-bootstrap"
pkgver = "1.76.0"
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
            "6e2998b0a5452c38d56b820a92042cb63fcef5a98ab38246b9f4c311cc9dd08b",
            "1dc1b09a6c91a29f8995bee5b9a4e7397dd347bc64aa3693dcaeb16189daff9c",
        ]
    case "ppc64le":
        sha256 = [
            "e597e0a424d1d861e3b833d55aec2d831f9806d1db6409b7497cc384b44a4ba6",
            "36d732c32504d02307e1527d920b0c1caaf0e317f694d3c8963575f45b99a23b",
        ]
    case "ppc64":
        sha256 = [
            "968c0320304f0d866917c2120229bc4fded5f648cb740e9339a18fae7467a953",
            "cbb8a5652172bb1a0a3f197c44f4119e8d040e8eab895d5aa883a99316f411ce",
        ]
    case "riscv64":
        sha256 = [
            "7d7faecd8b87eedfe700c5beb14519cde0c1e5fdb7a8d6f138cf3dbde460f26c",
            "0275b20639aa111b7f5107be28a3a1cc46e2043190cae1218e44073a728b74ae",
        ]
    case "x86_64":
        sha256 = [
            "d6a5613c7dfafeec8163783afb81ca9f01efce7256ab48fe946b909a4b59dd73",
            "e49fa65e248ed7d08b53ca9dec8ed552d40a87b3810ae3582e87c0e16c1e08ac",
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
