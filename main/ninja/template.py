pkgname = "ninja"
pkgver = "1.10.2"
pkgrel = 0
hostmakedepends = ["python"]
pkgdesc = "Small build system with a focus on speed"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://ninja-build.org"
source = f"https://github.com/ninja-build/ninja/archive/v{pkgver}.tar.gz"
sha256 = "ce35865411f0490368a8fc383f29071de6690cbadc27704734978221f25e2bed"

def do_configure(self):
    self.do("python", "configure.py", "--bootstrap")

def do_build(self):
    self.do("python", "configure.py")

def do_check(self):
    self.do(self.chroot_cwd / "ninja", "ninja_test")
    self.do(
        self.chroot_cwd / "ninja_test",
        "--gtest_filter=-SubprocessTest.SetWithLots"
    )

def do_install(self):
    self.install_bin("ninja")
    self.install_file(
        "misc/bash-completion", "usr/share/bash-completion/completions",
        name = "ninja"
    )
    self.install_file(
        "misc/zsh-completion", "usr/share/zsh/site-functions", name = "_ninja"
    )
