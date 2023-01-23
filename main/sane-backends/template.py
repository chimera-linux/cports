pkgname = "sane-backends"
pkgver = "1.1.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-locking",
    "--enable-ipv6", "--enable-pthread",
    "--with-usb",
    "--docdir=/usr/share/doc/sane",
    "ac_cv_func_mmap_fixed_mapped=yes",
]
make_cmd = "gmake"
make_dir = "." # bad build system
hostmakedepends = ["gmake", "pkgconf", "python"]
makedepends = [
    "linux-headers",
    "libgphoto2-devel",
    "v4l-utils-devel",
    "libusb-devel",
    "openssl-devel",
    "libxml2-devel",
    "libcurl-devel",
    "avahi-devel",
    "libjpeg-turbo-devel",
    "libtiff-devel",
]
pkgdesc = "Scanner Access Now Easy"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later WITH custom:sane-exception"
url = "http://sane-project.org"
_rhash = "7d30fab4e115029d91027b6a58d64b43"
source = f"https://gitlab.com/sane-project/backends/uploads/{_rhash}/{pkgname}-{pkgver}.tar.gz"
sha256 = "dd4b04c37a42f14c4619e8eea6a957f4c7c617fe59e32ae2872b373940a8b603"
# unmarked api; FIXME int (fails tests)
hardening = ["!vis", "!int"]
# otherwise we get conflicting providers because all the
# plugins provide a libsane.so.1 soname for whatever reason
options = ["!scanshlibs"]
system_users = [
    {
        "name": "_saned",
        "id": None,
        "groups": ["lp", "scanner"]
    }
]

def post_install(self):
    self.install_license("LICENSE")

    self.install_service(self.files_path / "saned")

    self.install_file(
        self.files_path / "saned.xinetd", "etc/xinetd.d", name = "saned.conf"
    )
    self.install_file(
        "tools/udev/libsane.rules", "usr/lib/udev/rules.d",
        name = "49-sane.rules"
    )

@subpackage("libsane")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("sane-backends-devel")
def _devel(self):
    return self.default_devel()
