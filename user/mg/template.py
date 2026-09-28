pkgname = "mg"
pkgver = "20260719"
pkgrel = 0
build_style = "makefile"
make_install_args = ["prefix=/usr", "mandir=$(prefix)/share/man"]
hostmakedepends = ["pkgconf"]
makedepends = ["ncurses-devel", "libbsd-devel"]
pkgdesc = "Micro GNU Emacs"
license = "custom:none"
url = "https://github.com/hboetes/mg"
source = f"https://github.com/hboetes/mg/archive/{pkgver}.tar.gz"
sha256 = "8ca736b1e57d9681e7921d37b9cf0282e3098e2929ed37384400c78dae54762d"
# crashes on enter
hardening = ["!int"]
# no tests
options = ["!check"]
