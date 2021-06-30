pkgname = "bsdutils"
_commit="cd3f2427f59d40851d0781ae5e9c1cd479ffade4"
version = "0.0.1"
revision = 3
wrksrc = f"bsdutils-{_commit}"
bootstrap = True
build_style = "meson"
makedepends = [
    "acl-devel", "ncurses-devel", "libedit-devel", "openssl-devel",
    "musl-fts-devel", "musl-rpmatch-devel", "libxo-devel"
]
short_desc = "Alternative to GNU coreutils from FreeBSD"
maintainer = "q66 <daniel@octaforge.org>"
license = "BSD-2-Clause"
homepage = "https://github.com/chimera-linux/bsdutils"
distfiles = [f"https://github.com/chimera-linux/bsdutils/archive/{_commit}.tar.gz"]
checksum = ["cb03da705357ee2b24a55f3ccae9943749e1f39bdc9f574972842637f9dfa988"]

if not current.bootstrapping:
    hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
