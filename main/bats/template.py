pkgname = "bats"
pkgver = "1.11.1"
pkgrel = 0
hostmakedepends = ["bash"]
checkdepends = ["bash", "procps"]
depends = ["bash"]
pkgdesc = "Bash Automated Testing System"
maintainer = "hge <h.gersen@gmail.com>"
license = "MIT"
url = "https://github.com/bats-core/bats-core"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5c57ed9616b78f7fd8c553b9bae3c7c9870119edd727ec17dbd1185c599f79d9"


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
