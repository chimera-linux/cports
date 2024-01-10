pkgname = "skkdict"
pkgver = "0_git20231226"
pkgrel = 0
_commit = "b7de5cd70aac106d9dd20898531357fbf4ca4707"
pkgdesc = "SKK japanese dictionary files"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Unicode-DFS-2016"
url = "http://openlab.jp/skk/dic.html"
source = f"https://github.com/skk-dev/dict/archive/{_commit}.tar.gz"
sha256 = "c754fba1e7857151626216a837e4c83d254826f89bd4d73bc857e0dd2a9adda0"
# no tests
options = ["!check"]


def do_install(self):
    self.install_file("SKK-JISYO.*", "usr/share/skk", glob=True)
