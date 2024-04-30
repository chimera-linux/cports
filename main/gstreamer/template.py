pkgname = "gstreamer"
pkgver = "1.24.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dptp-helper-permissions=none",  # manual
    "-Dpackage-origin=https://chimera-linux.org",
    "-Ddbghelp=disabled",
    "-Dintrospection=enabled",
    "-Ddefault_library=shared",
]
make_check_args = ["--timeout-multiplier", "4"]
hostmakedepends = [
    "bison",
    "docbook-xsl-nons",
    "flex",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libcap-progs",
    "meson",
    "pkgconf",
    "python",
    "rust",
]
makedepends = [
    "bash-completion",
    "glib-devel",
    "libcap-devel",
    "libxml2-devel",
    "rust-std",
]
pkgdesc = "Core GStreamer libraries and elements"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1225ef4a329fae1cadc5ec727dab249ad567e8072879493561ceb91ed34aa414"
file_modes = {
    "usr/libexec/gstreamer-1.0/gst-ptp-helper": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/libexec/gstreamer-1.0/gst-ptp-helper": {
        "security.capability": "cap_net_bind_service,cap_net_admin+ep",
    },
}
options = ["!cross"]


@subpackage("gstreamer-devel")
def _devel(self):
    return self.default_devel(
        extra=["usr/share/gdb", "usr/share/gstreamer-1.0"]
    )
