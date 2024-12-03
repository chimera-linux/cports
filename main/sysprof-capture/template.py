# sync with main/sysprof
pkgname = "sysprof-capture"
pkgver = "47.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=false",
    "-Dgtk=false",
    "-Dhelp=false",
    "-Dtools=false",
    "-Dtests=false",
    "-Dsysprofd=none",
    "-Dlibsysprof=false",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-headers"]
# .a + .pc + .h moved into here
replaces = ["sysprof-devel<47.0-r1", "sysprof-devel-static<47.0-r1"]
pkgdesc = "System-wide profiler for Linux"
subdesc = "static capture library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-2-Clause-Patent"
url = "https://www.sysprof.com"
source = f"$(GNOME_SITE)/sysprof/{'.'.join(pkgver.rsplit('.')[:-1])}/sysprof-{pkgver}.tar.xz"
sha256 = "e4b5ede9fd978ec3f0d5a0d44d0429a6d201c362bf6cb4527319031ae462c54f"
# sysprof`sysprof_disk_usage_record_fiber muloverflow when busy i/o
hardening = ["!int"]
# static lib only
options = ["!lto"]


def post_install(self):
    self.install_license("src/libsysprof-capture/COPYING")
