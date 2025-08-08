pkgname = "libcamera"
pkgver = "0.5.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtest=true"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "python-jinja2",
    "python-ply",
    "python-pyyaml",
]
makedepends = [
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtest-devel",
    "libevent-devel",
    "libunwind-devel",
    "libyaml-devel",
    "openssl3-devel",
    "udev-devel",
]
pkgdesc = "Open source camera stack and framework"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://libcamera.org"
source = f"https://github.com/libcamera-org/libcamera/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cab2196b55487cfc27a1cbf0f83eb420194d280bb44cc6c88a1311ff154844d1"
nostrip_files = ["usr/lib/libcamera/ipa*.so"]


def post_install(self):
    from cbuild.util import strip

    for f in (self.destdir / "usr/lib/libcamera").glob("ipa*.so"):
        fr = f.relative_to(self.destdir)
        print(f"   Stripping and signing: {fr.name}")
        strip.strip_attach(self, [fr])
        self.do(
            "src/ipa/ipa-sign.sh",
            "build/src/ipa-priv-key.pem",
            self.chroot_destdir / fr,
            f"{self.chroot_destdir / fr}.sign",
        )


@subpackage("libcamera-gstreamer")
def _(self):
    self.subdesc = "GStreamer support"
    self.install_if = [self.parent, "gstreamer"]
    self.renames = ["gstreamer-libcamera"]
    return ["usr/lib/gstreamer-1.0"]


@subpackage("libcamera-devel")
def _(self):
    return self.default_devel(extra=["usr/bin/lc-compliance"])
