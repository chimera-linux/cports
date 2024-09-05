pkgname = "sysprof"
pkgver = "47_beta"
pkgrel = 0
build_style = "meson"
configure_args = [
    # creates static separately itself
    "-Ddefault_library=shared",
    "-Dsystemdunitdir=systemd",
    "-Dexamples=false",
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
pkgdesc = "System-wide profiler for Linux"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://www.sysprof.com"
source = f"$(GNOME_SITE)/sysprof/{pkgver[:2]}/sysprof-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "e4d9178d7d941696e0ab6341645191f7cf929126ff2d6a8a209cb328ee59372c"
# sysprof`sysprof_disk_usage_record_fiber muloverflow when busy i/o
hardening = ["!int"]


def post_install(self):
    self.install_service(self.files_path / "sysprof")
    self.uninstall("usr/systemd")


@subpackage("sysprof-devel-static")
def _(self):
    return ["usr/lib/*.a"]


@subpackage("sysprof-devel")
def _(self):
    self.depends += [self.with_pkgver("sysprof-devel-static")]
    return self.default_devel()
