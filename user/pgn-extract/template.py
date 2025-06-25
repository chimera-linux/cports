pkgname = "pgn-extract"
pkgver = "25.01"
pkgrel = 0
build_style = "makefile"
make_build_args = ["OPTIMISE="]
make_check_target = "all"
make_check_args = ["--directory", "test"]
make_use_env = True
pkgdesc = "Portable Game Notation (PGN) Manipulator for Chess Games"
license = "GPL-3.0-or-later"
url = "https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract"
source = f"{url}/pgn-extract-{pkgver.replace('.', '-')}.tgz"
sha256 = "c024a2d64abaedc873bd4e70b19d3ffdbbfa4dd054e6856b4a4262238af10eaa"


def post_extract(self):
    self.mv("pgn-extract/*", ".", glob=True)
    self.rm("pgn-extract", recursive=True)


def init_build(self):
    self.make_build_args += ["ORIGCFLAGS=" + self.get_cflags(shell=True)]


def install(self):
    self.install_bin("pgn-extract")
    self.install_man("pgn-extract.man", "pgn-extract", 1)
    self.install_file("help.html", "usr/share/doc/pgn-extract")
