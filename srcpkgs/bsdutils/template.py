pkgname = "bsdutils"
_commit="ca01cc92a62a58b5f3111151d33ff13f1b7ce0e0"
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
checksum = ["b2f175d7c25edd6b3969da634279b5c4ec837964a1ab3a47bea69806d536215d"]

if not current.bootstrapping:
    hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
