pkgname = "pgn-extract"
pkgver = "24.10"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["OPTIMISE="]
make_check_target = "all"
make_check_args = ["--directory", "test"]
make_use_env = True
hostmakedepends = ["gmake"]
pkgdesc = "Portable Game Notation (PGN) Manipulator for Chess Games"
maintainer = "shtayerc <david.murko@mailbox.org>"
license = "GPL-3.0-or-later"
url = "https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract"
source = f"{url}/pgn-extract-{pkgver.replace('.', '-')}.tgz"
sha256 = "f15ab628218111e048b6d9313ea519f03125edd6edf2c860811246d5da921279"


def init_build(self):
    self.make_build_args += ["ORIGCFLAGS=" + self.get_cflags(shell=True)]


def do_install(self):
    self.install_bin("pgn-extract")
    self.install_man("pgn-extract.man", "pgn-extract", 1)
    self.install_file("help.html", "usr/share/doc/pgn-extract")
