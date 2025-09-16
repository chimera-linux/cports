pkgname = "icecream"
pkgver = "1.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--enable-shared"]
hostmakedepends = [
    "asciidoc",
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
    "libarchive-devel",
    "libcap-ng-devel",
    "lzo-devel",
    "zstd-devel",
]
depends = [
    "cmd:ugetopt!ugetopt",
]
pkgdesc = "Distributed compiler"
license = "GPL-2.0-or-later"
url = "https://github.com/icecc/icecream"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "249dcf74f0fc477ff9735ff0bdcdfaa4c257a864c4db5255d8b25c9f4fd20b6b"


def post_install(self):
    self.install_service(self.files_path / "icecc-scheduler")
    self.install_service(self.files_path / "iceccd")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("icecream-devel")
def _(self):
    return self.default_devel()
