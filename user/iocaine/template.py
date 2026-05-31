pkgname = "iocaine"
pkgver = "3.1.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "ai.robots.txt",
    "dinit-chimera",
    "fennel",
    "rust-std",
    "zstd-devel",
]
pkgdesc = "LLM crawler abuse defense mechanism"
license = "MIT"
url = "https://iocaine.madhouse-project.org"
source = f"https://git.madhouse-project.org/iocaine/iocaine/archive/iocaine-{pkgver}.tar.gz"
sha256 = "c37cbbf489adecafee67ee9a17fef48b8a8aa8cf27bb7b3401ab96c64225ac78"


def post_extract(self):
    self.mkdir("data/defaults/etc", parents=True)
    self.cp(
        self.bldroot_path / "usr/share/ai.robots.txt/robots.json",
        "data/defaults/etc",
    )
    self.cp(
        self.bldroot_path / "usr/bin/fennel", "data/defaults/etc/fennel.lua"
    )
    self.chmod("data/defaults/etc/fennel.lua", 0o644)


def install(self):
    self.install_license("LICENSES/MIT.txt")
    self.install_bin(f"target/{self.profile().triplet}/release/iocaine")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "iocaine")
