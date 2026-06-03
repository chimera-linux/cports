pkgname = "bats"
pkgver = "1.13.0"
pkgrel = 0
hostmakedepends = ["bash"]
checkdepends = ["bash", "procps"]
depends = ["bash"]
pkgdesc = "Bash Automated Testing System"
license = "MIT"
url = "https://github.com/bats-core/bats-core"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a85e12b8828271a152b338ca8109aa23493b57950987c8e6dff97ba492772ff3"


def post_extract(self):
    for f in (self.cwd / "libexec/bats-core").iterdir():
        self.mv(f, "lib/bats-core")
    # for tests
    self.rm("libexec", recursive=True)
    self.ln_s("lib", "libexec")
    # cba to patch
    self.rm("test/install.bats")


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
