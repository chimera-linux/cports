pkgname = "bats"
pkgver = "1.12.0"
pkgrel = 0
hostmakedepends = ["bash"]
checkdepends = ["bash", "procps"]
depends = ["bash"]
pkgdesc = "Bash Automated Testing System"
license = "MIT"
url = "https://github.com/bats-core/bats-core"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e36b020436228262731e3319ed013d84fcd7c4bd97a1b34dee33d170e9ae6bab"


def check(self):
    self.do(
        "./bin/bats",
        "--tap",
        "test",
        env={"TERM": "dumb"},
    )


def install(self):
    self.do(
        "./install.sh",
        self.chroot_destdir / "usr",
    )
    self.install_license("LICENSE.md")
