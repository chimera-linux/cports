pkgname = "lmdb"
pkgver = "0.9.31_git20240129"
pkgrel = 0
# literally forgot to tag this.. so just pretend it's git cause there's bugfixes in it
_gitrev = "e96d8dfa3951c06062a6fffbe1d7a2f3c9c1ff76"
build_wrksrc = "libraries/liblmdb"
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["prefix=/usr"]
make_check_target = "test"
make_check_env = {"LD_LIBRARY_PATH": "."}
make_use_env = True
hostmakedepends = [
    "gmake",
    "pkgconf",
]
pkgdesc = "Lightning Memory-Mapped Database Manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OLDAP-2.8"
url = "http://www.lmdb.tech/doc"
source = f"https://github.com/LMDB/lmdb/archive/{_gitrev}.tar.gz"
sha256 = "6c8197c7f473953941cb49070d24e7318ec465b8a0224c284876db646bb8ede0"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("COPYRIGHT")
    self.install_file(self.files_path / "lmdb.pc", "usr/lib/pkgconfig")


@subpackage("lmdb-devel")
def _devel(self):
    return self.default_devel()
