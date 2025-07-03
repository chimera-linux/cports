# sync with main/sysprof
pkgname = "sysprof-capture"
pkgver = "48.0"
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
license = "BSD-2-Clause-Patent"
url = "https://www.sysprof.com"
source = f"$(GNOME_SITE)/sysprof/{'.'.join(pkgver.rsplit('.')[:-1])}/sysprof-{pkgver}.tar.xz"
sha256 = "1b0f0380f2f30708ba87829321a06fee1db36dfa87797bbf07f0a7acf4498d18"
# sysprof`sysprof_disk_usage_record_fiber muloverflow when busy i/o
hardening = ["!int"]
# static lib only
options = ["!lto"]


def post_install(self):
    self.install_license("src/libsysprof-capture/COPYING")
