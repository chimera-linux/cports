pkgname = "libtraceevent"
pkgver = "1.8.3"
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
sha256 = "233d88adf5bae6b4511980f0f6314f348326b55fdb3dc9c4212c810e1ab06789"
# vis breaks symbols
hardening = ["!vis"]


@subpackage("libtraceevent-devel")
def _devel(self):
    return self.default_devel()
