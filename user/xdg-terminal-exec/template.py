pkgname = "xdg-terminal-exec"
pkgver = "0.14.4"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr"]
make_check_target = "test"
hostmakedepends = [
    "scdoc",
]
checkdepends = [
    "bats",
]
pkgdesc = "XDG default terminal launcher"
license = "GPL-3.0-or-later"
url = "https://github.com/Vladimir-csp/xdg-terminal-exec"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "10e079032396a386dabcec5627893db17dc3c76c12318b3719d78f3b70aa7ef4"
