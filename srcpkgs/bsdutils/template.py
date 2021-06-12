pkgname = "bsdutils"
_commit="459414732b474a5c451771d2ccffb34d2224a4e0"
version = "0.0.1"
revision = 1
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
checksum = ["fb007a201c8bcc2c164cfdb7ddb0821bfc629d2ed4fdd921f5495f8245af1884"]

if not current.bootstrapping:
    hostmakedepends = ["flex", "byacc", "meson", "pkgconf"]
