pkgname = "bsdgrep"
pkgver = "1.0.4"
pkgrel = 0
build_style = "makefile"
makedepends = ["bzip2-devel", "zlib-devel", "musl-fts-devel"]
pkgdesc = "FreeBSD grep(1)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/chimera-linux/bsdgrep"
sources = [f"https://github.com/chimera-linux/bsdgrep/archive/refs/tags/v{pkgver}.tar.gz"]
sha256 = ["839a505c5d5f6d53069e1863ed264d33120db01df29a606441a67cd40ce032ea"]

options = ["bootstrap", "!check"]
