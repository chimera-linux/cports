pkgname = "etckeeper"
pkgver = "1.18.22"
pkgrel = 0
build_style = "makefile"
make_install_args = [
    "PYTHON=/bin/false",
    "zshcompletiondir=${prefix}/share/zsh/site-functions",
]
make_check_target = "test"
checkdepends = ["bats", "fakeroot", "git"]
depends = ["git"]
pkgdesc = "Store /etc in git"
maintainer = "hge <h.gersen@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://etckeeper.branchable.com"
source = f"https://git.joeyh.name/index.cgi/etckeeper.git/snapshot/etckeeper-{pkgver}.tar.gz"
sha256 = "ff0e95e3b6cf6f377b8a04f18f572b011e890eedc1a742b3c0e11ebc283f7a7e"
