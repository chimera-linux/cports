pkgname = "icecream"
pkgver = "1.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-shared"]
make_cmd = "gmake"
hostmakedepends = [
    "asciidoc",
    "automake",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "libarchive-devel",
    "libcap-ng-devel",
    "lzo-devel",
    "zstd-devel",
]
depends = [
    "virtual:cmd:ugetopt!ugetopt",
]
pkgdesc = "Distributed compiler"
maintainer = "Erica Z <zerica@callcc.eu>"
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
def _devel(self):
    return self.default_devel()
