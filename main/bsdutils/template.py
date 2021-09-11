pkgname = "bsdutils"
_commit="0c83b868c95e598613326bc365262fd0456f0088"
version = "0.0.1"
revision = 0
wrksrc = f"bsdutils-{_commit}"
build_style = "meson"
makedepends = [
    "acl-devel", "ncurses-devel", "libedit-devel", "openssl-devel",
    "musl-fts-devel", "musl-rpmatch-devel", "libxo-devel"
]
short_desc = "Alternative to GNU coreutils from FreeBSD"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdutils"
distfiles = [f"https://github.com/chimera-linux/bsdutils/archive/{_commit}.tar.gz"]
checksum = ["025a4bc07bf530eae627f3c6926875344c382a2808ad1a77d81dc5b1ee30622e"]

options = ["bootstrap", "!check"]

if not current.bootstrapping:
    hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
