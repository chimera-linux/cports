pkgname = "lmdbxx"
pkgver = "1.0.0"
pkgrel = 0
build_style = "makefile"
# makefile build style doesn't set these for check so it enables sanitizers for
# the test
make_check_args = ["LDFLAGS=", "CXXFLAGS="]
makedepends = ["lmdb-devel"]
depends = [*makedepends]
pkgdesc = "Header-only C++ wrapper for LMDB"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Unlicense"
url = "https://github.com/hoytech/lmdbxx"
source = f"https://github.com/hoytech/lmdbxx/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5e12eb3aefe9050068af7df2c663edabc977ef34c9e7ba7b9d2c43e0ad47d8df"
