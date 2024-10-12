pkgname = "libtraceevent"
pkgver = "1.8.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    # builds both libtracevent.so and loadable plugins,
    # with static also outputs useless .a plugins in
    # /usr/lib/libtracevent/
    "-Ddefault_library=shared",
]
hostmakedepends = [
    "asciidoc",
    "meson",
    "pkgconf",
    "xmlto",
]
makedepends = ["cunit-devel", "linux-headers"]
pkgdesc = "Linux kernel trace event library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-only AND GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git"
source = f"{url}/snapshot/libtraceevent-{pkgver}.tar.gz"
sha256 = "dc456d4d2bf4b4cd4d0c737d3374a8093f9e5ca18c1d7fc2279a4bf41e613121"
# vis breaks symbols
hardening = ["!vis"]


@subpackage("libtraceevent-devel")
def _(self):
    return self.default_devel()
