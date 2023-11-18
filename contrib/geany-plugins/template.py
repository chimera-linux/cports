pkgname = "geany-plugins"
pkgver = "2.0.0"
pkgrel = 2
build_style = "gnu_configure"
configure_args = [
    "--enable-all-plugins",
    "--disable-geniuspaste",  # libsoup 2.x
    "--disable-updatechecker",  # libsoup 2.x
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "glib-devel",
    "gettext-devel",
    "gmake",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = [
    "ctpl-devel",
    "enchant-devel",
    "geany-devel",
    "gpgme-devel",
    "libgit2-devel",
    "lua5.1-devel",
    "vte-gtk3-devel",
    "webkitgtk-devel",
    "zlib-devel",
]
depends = [f"geany~{pkgver}"]
pkgdesc = "Geany IDE plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://geany.org"
source = f"https://github.com/geany/geany-plugins/releases/download/{pkgver}/geany-plugins-{pkgver[:-2]}.tar.gz"
sha256 = "cd7d27f00aef4afe2040d7e5246a863234c340c8520ef698be9a15005ed8f57e"

if self.profile().arch == "aarch64":
    # work around builtins not being linked properly
    tool_flags = {
        "CXXFLAGS": ["-mno-outline-atomics"],
        "CFLAGS": ["-mno-outline-atomics"],
    }
