pkgname = "libspelling"
pkgver = "0.3.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denchant=enabled",
    "-Dvapi=true",
    "-Ddocs=false",
    "-Dsysprof=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "vala",
    "glib-devel",
]
makedepends = [
    "enchant-devel",
    "glib-devel",
    "gtk4-devel",
    "gtksourceview-devel",
    "icu-devel",
]
checkdepends = ["enchant"]
pkgdesc = "Spellcheck library for GTK 4"
maintainer = "GeopJr <evan@geopjr.dev>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libspelling"
source = f"$(GNOME_SITE)/libspelling/{pkgver[:3]}/libspelling-{pkgver}.tar.xz"
sha256 = "b33f81039d8edda15f0e740ab263dea85ea363af4440e81e97789716c6f111c0"
# FIXME check: traps: test-engine[12617] trap int3 ip:7f317b116cdc sp:7ffc07e12800 error:0 in libglib-2.0.so.0.8200.0[108cdc,7f317b0b1000+e3000]
# 2/4 test-engine        FAIL            0.01s   killed by signal 5 SIGTRAP
# >>> MSAN_OPTIONS=halt_on_error=1:abort_on_error=1:print_summary=1:print_stacktrace=1 ASAN_OPTIONS=halt_on_error=1:abort_on_error=1:print_summary=1 GSETTINGS_BACKEND=memory UBSAN_OPTIONS=halt_on_error=1:abort_on_error=1:print_summary=1:print_stacktrace=1 MESON_TEST_ITERATION=1 G_DEBUG=gc-friendly MALLOC_PERTURB_=240 MALLOC_CHECK_=2 /builddir/libspelling-0.3.1/build/testsuite/test-engine
options = ["!check"]


@subpackage("libspelling-devel")
def _(self):
    return self.default_devel()
