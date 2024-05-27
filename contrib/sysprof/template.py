pkgname = "sysprof"
pkgver = "46.0"
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
sha256 = "73aa7e75ebab3e4e0946a05a723df7e6ee4249e3b9e884dba35500aba2a1d176"


def post_install(self):
    self.install_service(self.files_path / "sysprof")
    self.rm(self.destdir / "usr/systemd", recursive=True)


@subpackage("sysprof-devel")
def _devel(self):
    return self.default_devel()
