pkgname = "libidn2"
pkgver = "2.3.8"
pkgrel = 0
build_style = "gnu_configure"
# defines this to nothing and yields #if invalid syntax for some reason
make_build_args = ["GNULIBHEADERS_OVERRIDE_WINT_T=0"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = ["libunistring-devel"]
pkgdesc = "Internationalized string handling library"
license = "LGPL-3.0-or-later AND GPL-3.0-or-later"
url = "https://www.gnu.org/software/libidn#libidn2"
source = f"$(GNU_SITE)/libidn/libidn2-{pkgver}.tar.gz"
sha256 = "f557911bf6171621e1f72ff35f5b1825bb35b52ed45325dcdee931e5d3c0787a"


@subpackage("libidn2-devel")
def _(self):
    return self.default_devel(
        extra=[
            "usr/share/info",
        ]
    )


@subpackage("libidn2-progs")
def _(self):
    return self.default_progs()
