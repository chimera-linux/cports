pkgname = "bats"
pkgver = "1.11.0"
pkgrel = 0
hostmakedepends = ["bash"]
checkdepends = ["bash", "procps"]
depends = ["bash"]
pkgdesc = "Bash Automated Testing System"
maintainer = "hge <h.gersen@gmail.com>"
license = "MIT"
url = "https://github.com/bats-core/bats-core"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "aeff09fdc8b0c88b3087c99de00cf549356d7a2f6a69e3fcec5e0e861d2f9063"


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
