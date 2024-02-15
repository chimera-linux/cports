pkgname = "libtraceevent"
pkgver = "1.8.2"
pkgrel = 2
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
sha256 = "919f0c024c7b5059eace52d854d4df00ae7e361a4033e1b4d6fe01d97064a1b9"
# vis breaks symbols
hardening = ["!vis"]


@subpackage("libtraceevent-devel")
def _devel(self):
    return self.default_devel()
