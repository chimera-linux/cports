# ensure soname for links matches and manifest file is updated
pkgname = "openh264"
pkgver = "2.6.0"
pkgrel = 1
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
license = "BSD-2-Clause"
url = "https://github.com/cisco/openh264"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    "https://github.com/mozilla/gmp-api/archive/refs/tags/Firefox135.tar.gz",
]
source_paths = [".", "gmp-api"]
sha256 = [
    "558544ad358283a7ab2930d69a9ceddf913f4a51ee9bf1bfb9e377322af81a69",
    "939be3596292ff445bf3cd5454a03041f68258444f7fff023a0bac17b238b40f",
]


match self.profile().arch:
    case "aarch64" | "armv7" | "x86*":
        make_build_args += ["USE_ASM=Yes"]
    case _:
        make_build_args += ["USE_ASM=NO"]


def post_install(self):
    self.install_license("LICENSE")
    _nspath = "usr/lib/nsbrowser/plugins/gmp-gmpopenh264/system-installed"
    # grab the main pkgver lib
    self.install_file(
        f"libgmpopenh264.so.{pkgver}",
        _nspath,
    )
    # symlinks; ensure the soname is right
    self.install_link(
        f"{_nspath}/libgmpopenh264.so.8", f"libgmpopenh264.so.{pkgver}"
    )
    self.install_link(f"{_nspath}/libgmpopenh264.so", "libgmpopenh264.so.8")
    # manifest file
    self.install_file(self.files_path / "gmpopenh264.info", _nspath)
    # profile and other stuff
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
