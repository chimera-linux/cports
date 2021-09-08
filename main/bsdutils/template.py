pkgname = "bsdutils"
_commit="3c2d40f9a1cf0803e77f130953aabf26aa2f738c"
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
checksum = ["a9e6c7e0c4277e323d19b0730b99c42f7e8a012ac33882ac7a5b3db179f0188f"]

options = ["bootstrap", "!check"]

if not current.bootstrapping:
    hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
