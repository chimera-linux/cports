pkgname = "libcamera"
pkgver = "0.1.0"
pkgrel = 1
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
sha256 = "6d9b0f33939de29a2d8950924f82713981b890f9b5dc1d68a65db76a1222b15a"
nostrip_files = ["usr/lib/libcamera/ipa*.so"]


def post_install(self):
    from cbuild.util import strip

    for f in (self.destdir / "usr/lib/libcamera").glob("ipa*.so"):
        print(f"   Stripping and signing: {f.name}")
        strip.strip_attach(self, f)
        self.do(
            "src/ipa/ipa-sign.sh",
            "build/src/ipa-priv-key.pem",
            self.chroot_destdir / f.relative_to(self.destdir),
            f"{self.chroot_destdir / f.relative_to(self.destdir)}.sign",
        )


@subpackage("gstreamer-libcamera")
def _gst(self):
    self.pkgdesc = f"{pkgdesc} (GStreamer support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "gstreamer"]
    return ["usr/lib/gstreamer-1.0"]


@subpackage("libcamera-devel")
def _devel(self):
    return self.default_devel(extra=["usr/bin/lc-compliance"])
