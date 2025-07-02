pkgname = "jq"
pkgver = "1.8.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["oniguruma-devel"]
pkgdesc = "Command-line JSON processor"
license = "MIT"
url = "https://github.com/jqlang/jq"
source = f"{url}/releases/download/jq-{pkgver}/jq-{pkgver}.tar.gz"
sha256 = "2be64e7129cecb11d5906290eba10af694fb9e3e7f9fc208a311dc33ca837eb0"
# FIXME int: null meme in jqtest
# FIXME vis: fails to link
hardening = ["!int", "!vis", "!cfi"]


def post_extract(self):
    with (self.cwd / "VERSION").open("w") as vf:
        vf.write(pkgver)


def post_install(self):
    self.install_license("COPYING")
    # cfi staticlib
    self.uninstall("usr/lib/libjq.a")


@subpackage("jq-devel")
def _(self):
    return self.default_devel()


@subpackage("jq-libs")
def _(self):
    return self.default_libs()
