pkgname = "libcamera"
pkgver = "0.3.2"
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
    "openssl-devel",
    "udev-devel",
]
pkgdesc = "Open source camera stack and framework"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://libcamera.org"
source = f"https://github.com/libcamera-org/libcamera/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d2c0a28749ec95b84866bbdad1cd71e7d7309560153f8b369d27c0b1de5b459a"
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


@subpackage("gstreamer-libcamera")
def _(self):
    self.subdesc = "GStreamer support"
    self.install_if = [self.parent, "gstreamer"]
    return ["usr/lib/gstreamer-1.0"]


@subpackage("libcamera-devel")
def _(self):
    return self.default_devel(extra=["usr/bin/lc-compliance"])
