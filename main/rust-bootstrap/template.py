pkgname = "rust-bootstrap"
pkgver = "1.91.0"
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
            "e977520b01e5dba66fc6f19d41bdc9558171cbc17c68dabc90ab20765ccf887b",
            "12f2f0dba784cd4258d883b92470db75d4a5556c4bb9b304164bd6a41ba79bd7",
        ]
    case "loongarch64":
        sha256 = [
            "fd691fc6bc8f5d19e1ed7de83edf5e40348ef02d7ddfd6ba7a2322fe1f04b385",
            "904bbf73afbe09c30ac7b400b058c3ea6491a6c2b2a382bea1d80f6600f7bd32",
        ]
    case "ppc64le":
        sha256 = [
            "7937c8fb8e3c239d1bdc0d401ddccecf5f4a8cf38bfd49481298a0e93a0c8ae4",
            "f618e19299a4cfa3ca2c0462d033dc92e896206046c65697af1392afc4a829c0",
        ]
    case "ppc64":
        sha256 = [
            "e71e4b64bccb848afa2a3ef6d431eed88ab726a093ca2167bf8b6ec00f13bfb8",
            "28f8b1cdb275fdc04b487f724737f22e01647a38a580d368a9478f13628c7197",
        ]
    case "ppc":
        sha256 = [
            "c6256dcfd353e7d0c88bccd11f4e847af087629b7a68209dcc9183b59a244cbf",
            "75e99a7ef829c7b7935d96f3e69da528923f91d6ce633f0bc29595767fe205e1",
        ]
    case "riscv64":
        sha256 = [
            "f9c1392f091fe132d2edad4215dc157c9b3a0b92225243737e6262a85fbebb86",
            "5685f842be74efe0c5d30d3a1b38799d0a879172b09fc2345dc7fc4acac5fd38",
        ]
    case "x86_64":
        sha256 = [
            "721501bbcdf8294736f6716e80a98013e75b10d92df050cb6bca737ff8c9bf51",
            "34c827124850d1ea93a76c0c775476dd9de50585e2f90daa6bc8bcb8f5bf5b2a",
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
