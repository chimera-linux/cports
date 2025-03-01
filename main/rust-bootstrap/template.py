pkgname = "rust-bootstrap"
pkgver = "1.85.0"
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
            "d802e9014030391045182ba5ebde796058fc210a43fb45333dccb2fc9a549bcd",
            "f944abc58e7a65f29303e49b3b72096459dfd9153dcb9fb2f9035d2188015614",
        ]
    case "ppc64le":
        sha256 = [
            "72360f97785d65b8a5f4f5b694c69e76704f8ee232aeec74df03115dbf902aab",
            "0c906a291127cf7204e311fb7abde7d633da766a240faf08a942de45ecaf82ea",
        ]
    case "ppc64":
        sha256 = [
            "1d5266ef661f0db4eab2542d259a8f1a87be301f4e317c1684e027e67883f6b1",
            "8b0f9d964654c4d854ab9a46d04974512ba0bd91d4de26679ff2910452f2957f",
        ]
    case "ppc":
        sha256 = [
            "c6d711436bd3a50772c517e547babbbf737436a8a1e0a37bb6f70106f8eab0ec",
            "6b23afa36fbbe4b7812e57290b75ce73260fe8758e2831a959809fe25254d021",
        ]
    case "riscv64":
        sha256 = [
            "4cc02412e1c5f6b4ea9c75dab902acee0b9c9b08f110dd34ca03ef08107fa2bc",
            "009c3744b6cc3084f1b4682ae671512085f5d9c6d098aedc4fa93db43b41e818",
        ]
    case "x86_64":
        sha256 = [
            "444bbfc461a1d318a3be2dca383415f12d6cdc6296ae0586ac880dafb5b6d274",
            "4d0be071082cb53095538d90019e6cff91285d9e44216940ec47a4d00a9bae2a",
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
    for f in (self.destdir / f"usr/lib/rustlib/{trip}/bin").iterdir():
        f.unlink()
    # licenses
    self.install_license(f"rustc-{pkgver}-{self.profile().triplet}/LICENSE-MIT")
