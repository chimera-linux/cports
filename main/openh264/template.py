pkgname = "openh264"
pkgver = "2.5.0"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    f"ARCH={self.profile().arch}",
    "BUILDTYPE=Release",
    "CFLAGS_OPT=",
    "ENABLEPIC=Yes",
    "HAVE_AVX2=No",
    "HAVE_GMP_API=Yes",
    "libraries",
    "plugin",
]
make_check_target = "test"
make_use_env = True
hostmakedepends = ["nasm", "pkgconf"]
pkgdesc = "H.264 codec implementation"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://github.com/cisco/openh264"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    "https://github.com/mozilla/gmp-api/archive/refs/tags/Firefox114_2.tar.gz",
]
source_paths = [".", "gmp-api"]
sha256 = [
    "94c8ca364db990047ec4ec3481b04ce0d791e62561ef5601443011bdc00825e3",
    "c7fd4ae00dfa19bdc485fe6bfd08a337e245ec0f16a52891bcdede39aca8aed3",
]


match self.profile().arch:
    case "aarch64" | "armv7" | "x86*":
        make_build_args += ["USE_ASM=Yes"]
    case _:
        make_build_args += ["USE_ASM=NO"]


def post_install(self):
    self.install_license("LICENSE")
    # grab the main pkgver lib
    self.install_file(
        f"libgmpopenh264.so.{pkgver}",
        "usr/lib/nsbrowser/plugins/gmp-gmpopenh264/system-installed",
    )
    # then the symlinks. we can't use glob= install because it derefs the
    # symlinks and installs 3 copies of the same lib.
    self.install_file(
        "libgmpopenh264.so.7",
        "usr/lib/nsbrowser/plugins/gmp-gmpopenh264/system-installed",
    )
    self.install_file(
        "libgmpopenh264.so",
        "usr/lib/nsbrowser/plugins/gmp-gmpopenh264/system-installed",
    )

    self.install_file(
        self.files_path / "profile.conf",
        "etc/profile.d",
        name="firefox-openh264.sh",
    )
    self.install_file(
        self.files_path / "prefs.js",
        "usr/lib/firefox/defaults/pref",
        name="gmpopenh264.js",
    )


@subpackage("openh264-devel")
def _(self):
    return self.default_devel()


@subpackage("openh264-firefox-plugin")
def _(self):
    self.subdesc = "Plugin for Firefox"
    # installed in special path; the libgmpopenh264.so also has a soname of
    # libopenh264. just exclude it from providing stuff..
    self.options = ["!scanshlibs"]
    self.install_if = [self.with_pkgver("openh264-firefox-plugin-meta")]
    return [
        "etc/profile.d",
        "usr/lib/firefox",
        "usr/lib/nsbrowser",
    ]


@subpackage("openh264-firefox-plugin-meta")
def _(self):
    self.subdesc = "recommends package for firefox plugin"
    self.options = ["empty"]
    return []
