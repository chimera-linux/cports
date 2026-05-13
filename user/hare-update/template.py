pkgname = "hare-update"
pkgver = "0.26.0.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["LIBEXECDIR=/usr/lib"]  # XXX libexecdir
hostmakedepends = [
    f"binutils-{self.profile().arch}",
    "hare",
]
makedepends = ["hare"]
pkgdesc = "Hare add-on which assists in migrating codebases"
license = "EUPL-1.2"
url = "https://git.sr.ht/~sircmpwn/hare-update"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "08eed452da9ced4371167378761f3760d2f515e0a3ca3732d28b14d522920bcb"
tools = {"AS": f"{self.profile().triplet}-as"}
