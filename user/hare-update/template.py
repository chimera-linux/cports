pkgname = "hare-update"
pkgver = "0.25.2.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["LIBEXECDIR=/usr/lib"]  # XXX libexecdir
hostmakedepends = [
    f"binutils-{self.profile().arch}",
    "hare",
]
makedepends = ["hare"]
pkgdesc = "Hare add-on which assists in migrating condebases"
license = "EUPL-1.2"
url = "https://git.sr.ht/~sircmpwn/hare-update"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "48ca5aba4b36c07145976c1f3d9d3ac8b79a29f0bdfdac6de57bd138ed1d407c"
tools = {"AS": f"{self.profile().triplet}-as"}
