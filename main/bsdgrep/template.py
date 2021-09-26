pkgname = "bsdgrep"
version = "1.0.4"
revision = 0
build_style = "makefile"
makedepends = ["bzip2-devel", "zlib-devel", "musl-fts-devel"]
short_desc = "FreeBSD grep(1)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdgrep"
distfiles = [f"https://github.com/chimera-linux/bsdgrep/archive/refs/tags/v{version}.tar.gz"]
checksum = ["839a505c5d5f6d53069e1863ed264d33120db01df29a606441a67cd40ce032ea"]

options = ["bootstrap", "!check"]
