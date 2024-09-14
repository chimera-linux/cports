pkgname = "audiofile"
pkgver = "0.3.6"
pkgrel = 0
_commit = "2f4e4704b731086b11175c433e036bcbe7c9c913"
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool", "asciidoc"]
makedepends = ["alsa-lib-devel", "flac-devel", "linux-headers"]
pkgdesc = "Library for reading and writing audio files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://audiofile.68k.org"
source = f"https://github.com/sbaldovi/audiofile/archive/{_commit}.tar.gz"
sha256 = "a075d812e7fef5764934f11f8d5f0d583193db147f4075c0cdcd3292e054c66d"
# tests fail
hardening = ["!int"]


def pre_build(self):
    # racey as afQuery.3 also generates afQueryLong.3 etc
    self.do("make", "-j1", "-C", "docs")


@subpackage("audiofile-devel")
def _(self):
    return self.default_devel()
