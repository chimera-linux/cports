pkgname = "etckeeper"
pkgver = "1.18.21"
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
sha256 = "a87c5e9c847c29f761da933c1cd907779545c7ddf92fb75de8ef692b90fc9e5d"
