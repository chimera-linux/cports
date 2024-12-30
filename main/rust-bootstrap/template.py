pkgname = "rust-bootstrap"
pkgver = "1.83.0"
pkgrel = 0
# satisfy revdeps
makedepends = ["zlib-ng-compat", "ncurses-libs", "zstd"]
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
            "baa09647b4a3291abe5b4201550f522b0b02d246badd2350a5935bc86fc89671",
            "629ba7bf2e2a9499b79f7cdfee5a5d08c3f938b6eafc4ab2a7557035fb191908",
        ]
    case "ppc64le":
        sha256 = [
            "4a7e42ac8d218f9667f5dd5a3ac12304ba126202a8fc80dcfa08b76c27acf407",
            "2b855e5dba52a2483423ea0e68cc1d4616e622c4bc2325ed1e55971ded0a65da",
        ]
    case "ppc64":
        sha256 = [
            "938285d45a512cb57348852bec86f0109f1587039f92680bd9c359fab1a93eb2",
            "349f3ea7286d56709c0a8f4bc8c63d9cb30d923f98aaff68e8968a09466eb758",
        ]
    case "ppc":
        sha256 = [
            "08efd41c2ab5dca79bdc7e524f21ed591c6fd6620594fc0de601faa3b8ec1441",
            "11cdff6234d66ca202f54f2a839ebcf7c60a56b28ea7333637ca476db1617e80",
        ]
    case "riscv64":
        sha256 = [
            "d43faf829cff190883d8efaa9c6e74d304e8d231f9d41cd2958ebd4bf3e3abc5",
            "29d150a51d6212b184ae8c53651969082dc10e2a9ff3d2345143c106d8fc1000",
        ]
    case "x86_64":
        sha256 = [
            "736f83dc96006b85d49ba148ee26c8fcdbccd90045d1ee2e0162554b26c9c4ea",
            "88ad71f216ff8e285e9640be298e3f1843c461321ba65614b06f01b75345a8eb",
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
    for f in (self.destdir / f"usr/lib/rustlib/{trip}/bin").glob("rust-ll*"):
        f.unlink()
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
