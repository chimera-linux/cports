pkgname = "enlightenment"
pkgver = "0.25.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    # TODO: libexif
    "-Dpam=true", "-Dwl=true", "-Dsystemd=false", "-Dlibexif=false"
]
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny", "efl", "xwayland", "wayland-progs"
]
# TODO: bluetooth support
makedepends = [
    "gettext-tiny-devel", "efl-devel", "mesa-devel", "wayland-devel",
    "wayland-protocols", "libxkbcommon-devel", "linux-pam-devel",
    "xkeyboard-config"
]
depends = [
    "desktop-file-utils", "hicolor-icon-theme", "xkeyboard-config", "elogind"
]
pkgdesc = "Enlightenment desktop shell"
license = "BSD-2-Clause"
url = "https://enlightenment.org"
source = f"http://download.enlightenment.org/rel/apps/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2cf05fe3d96ef35e823619dbc0ac513ecabcae2186800ecd804924a637112444"
suid_files = [
    "usr/lib/enlightenment/utils/enlightenment_ckpasswd",
    "usr/lib/enlightenment/utils/enlightenment_system",
    "usr/lib/enlightenment/utils/enlightenment_sys",
]

def post_install(self):
    self.install_license("COPYING")

@subpackage("enlightenment-devel")
def _devel(self):
    self.depends += [f"enlightenment={pkgver}-r{pkgrel}"]

    return self.default_devel()
