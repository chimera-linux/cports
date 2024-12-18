pkgname = "reptyr"
pkgver = "0.10.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["BASHCOMPDIR=/usr/share/bash-completion/completions"]
make_check_target = "test"
make_check_args = ["PYTHON_CMD=python"]
makedepends = ["linux-headers"]
checkdepends = ["python-pexpect"]
pkgdesc = "Reparent a running program to a new terminal"
maintainer = "LeFantome <fantome137@proton.me>"
license = "MIT"
url = "https://github.com/nelhage/reptyr"
source = f"{url}/archive/refs/tags/reptyr-{pkgver}.tar.gz"
sha256 = "c6ffbc34a511ac00d072219bda30699e51f2f4eb483cbae9e32e981d49e8b380"
hardening = ["vis", "cfi"]
# ptrace_scope shenanigans prevent this on hardened hosts
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
