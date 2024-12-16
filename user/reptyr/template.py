pkgname = "reptyr"
pkgver = "0.10.0"
pkgrel = 0
build_style = "makefile"
makedepends = ["linux-headers"]
checkdepends = ["pkgconf", "python", "python-pexpect"]
pkgdesc = "Reparent a running program to a new terminal"
maintainer = "LeFantome <fantome137@proton.me>"
license = "MIT"
url = "https://github.com/nelhage/reptyr"
source = (
    f"https://github.com/nelhage/reptyr/archive/refs/tags/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "c6ffbc34a511ac00d072219bda30699e51f2f4eb483cbae9e32e981d49e8b380"
# Tests require additional permissions
options = ["!check"]


def patch(self):
    self.do("sed", "-i", """""", "-e", """s#python2#python3#""", "Makefile")
    self.do(
        "sed",
        "-i",
        """""",
        "-e",
        """s#etc/bash_completion.d#usr/share/bash-completion/completions#""",
        "Makefile",
    )


def check(self):
    self.do("make", "test")


def post_install(self):
    self.install_license("COPYING")
