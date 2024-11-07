# sync with main/sysprof-capture
pkgname = "sysprof"
pkgver = "47.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    # creates static separately itself
    "-Ddefault_library=shared",
    "-Dsystemdunitdir=systemd",
    "-Dexamples=false",
    # in sysprof-capture
    "-Dinstall-static=false",
]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "elogind-devel",
    "gtk4-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libdex-devel",
    "libpanel-devel",
    "libucontext-devel",
    "libunwind-nongnu-devel",
    "linux-headers",
    "polkit-devel",
]
depends = ["dinit-dbus"]
pkgdesc = "System-wide profiler for Linux"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later AND BSD-2-Clause-Patent"
url = "https://www.sysprof.com"
source = f"$(GNOME_SITE)/sysprof/{'.'.join(pkgver.rsplit('.')[:-1])}/sysprof-{pkgver}.tar.xz"
sha256 = "d3baba814be0cdaef28704c8004ff3110e99525422060f2a993a22a47b9334eb"
# sysprof`sysprof_disk_usage_record_fiber muloverflow when busy i/o
hardening = ["!int"]


def post_install(self):
    self.install_license("src/libsysprof-capture/COPYING")
    self.install_service(self.files_path / "sysprof")
    self.uninstall("usr/systemd")


@subpackage("sysprof-devel")
def _(self):
    return self.default_devel()
