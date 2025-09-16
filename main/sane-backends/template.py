pkgname = "sane-backends"
pkgver = "1.3.1"
pkgrel = 3
build_style = "gnu_configure"
configure_args = [
    "--disable-locking",
    "--enable-ipv6",
    "--enable-pthread",
    "--with-usb",
    "--docdir=/usr/share/doc/sane",
    "ac_cv_func_mmap_fixed_mapped=yes",
]
make_dir = "."  # bad build system
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = [
    "avahi-bootstrap",
    "curl-devel",
    "dinit-chimera",
    "libgphoto2-devel",
    "libjpeg-turbo-devel",
    "libtiff-devel",
    "libusb-devel",
    "libxml2-devel",
    "linux-headers",
    "openssl3-devel",
    "v4l-utils-devel",
]
pkgdesc = "Scanner Access Now Easy"
license = "GPL-2.0-or-later WITH custom:sane-exception"
url = "http://sane-project.org"
_rhash = "83bdbb6c9a115184c2d48f1fdc6847db"
source = f"https://gitlab.com/sane-project/backends/uploads/{_rhash}/sane-backends-{pkgver}.tar.gz"
sha256 = "aa82f76f409b88f8ea9793d4771fce01254d9b6549ec84d6295b8f59a3879a0c"
# FIXME int (fails tests)
hardening = ["!int"]
# otherwise we get conflicting providers because all the
# plugins provide a libsane.so.1 soname for whatever reason
# lto causes segfaults and usb scanner detection issues
options = ["!scanshlibs", "!lto"]


def post_install(self):
    self.install_license("LICENSE")

    self.install_service(self.files_path / "saned")
    self.install_sysusers(self.files_path / "saned.conf", name="saned")

    self.install_file(
        self.files_path / "saned.xinetd", "etc/xinetd.d", name="saned.conf"
    )
    self.install_file(
        "tools/udev/libsane.rules", "usr/lib/udev/rules.d", name="49-sane.rules"
    )


@subpackage("sane-backends-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libsane")]

    return self.default_libs()


@subpackage("sane-backends-devel")
def _(self):
    return self.default_devel()
