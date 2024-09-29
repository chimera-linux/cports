pkgname = "sysprof"
pkgver = "47.0"
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
source = f"$(GNOME_SITE)/sysprof/{'.'.join(pkgver.rsplit('.')[:-1])}/sysprof-{pkgver}.tar.xz"
sha256 = "7424c629434660654288c04248998c357d1ce87ee1559fd44df1980992ef5df5"
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
