pkgname = "bsdutils"
_commit="4f1cb254ad5549ddcaf2cf5cb2ceb5c84b839e52"
version = "0.0.1"
revision = 2
wrksrc = f"bsdutils-{_commit}"
bootstrap = True
build_style = "meson"
makedepends = [
    "acl-devel", "ncurses-devel", "libedit-devel", "openssl-devel",
    "musl-fts-devel", "musl-rpmatch-devel"
]
short_desc = "Alternative to GNU coreutils from FreeBSD"
maintainer = "q66 <daniel@octaforge.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdutils"
distfiles = [f"https://github.com/chimera-linux/bsdutils/archive/{_commit}.tar.gz"]
checksum = ["d464de8b3111aa794b43c08ef142d63ba46947bae481e07abb10b6cbfcba8ccb"]

if not current.bootstrapping:
    hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
