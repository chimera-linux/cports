pkgname = "gstreamer"
pkgver = "1.28.4"
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
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gstreamer/gstreamer-{pkgver}.tar.xz"
sha256 = "f5adc7e8f448c10260b3b25aa101c9d540674c8d9a54c2b77a86d04f2b3b50dd"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
file_modes = {
    "usr/lib/gstreamer-1.0/gst-ptp-helper": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/lib/gstreamer-1.0/gst-ptp-helper": {
        "security.capability": "cap_net_bind_service,cap_net_admin+ep",
    },
}
options = ["!cross"]


@subpackage("gstreamer-devel")
def _(self):
    return self.default_devel(
        extra=["usr/share/gdb", "usr/share/gstreamer-1.0"]
    )
