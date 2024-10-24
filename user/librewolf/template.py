pkgname = "librewolf"
pkgver = "131.0.3"
pkgrel = 0
hostmakedepends = [
    "automake",
    "cargo",
    "cbindgen",
    "clang-devel",
    "dbus",
    "gettext",
    "libtool",
    "llvm-devel",
    "nasm",
    "nodejs",
    "pkgconf",
    "python",
    "rust",
    "wasi-sdk",
    "xserver-xorg-xvfb",
    "zip",
]
makedepends = [
    "alsa-lib-devel",
    "dbus-devel",
    "ffmpeg-devel",
    "freetype-devel",
    "glib-devel",
    "gtk+3-devel",
    "icu-devel",
    "libevent-devel",
    "libffi-devel",
    "libjpeg-turbo-devel",
    "libnotify-devel",
    "libogg-devel",
    "libpng-devel",
    "libpulse-devel",
    "libtheora-devel",
    "libvorbis-devel",
    "libvpx-devel",
    "libwebp-devel",
    "libxcomposite-devel",
    "libxscrnsaver-devel",
    "libxt-devel",
    "mesa-devel",
    "nspr-devel",
    "nss-devel",
    "pipewire-jack-devel",
    "pixman-devel",
    "rust-std",
    "zlib-ng-compat-devel",
]
depends = [
    "libavcodec",
    "openh264-firefox-plugin-meta",
    "speechd-meta",
]
pkgdesc = "LibreWolf web browser"
maintainer = "anh0516 <anhollander516@gmail.com>"
license = "GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND MPL-2.0"
url = "https://librewolf.net"
source = f"https://gitlab.com/api/v4/projects/32320088/packages/generic/librewolf-source/{pkgver}-1/librewolf-{pkgver}-1.source.tar.gz"
sha256 = "6177f16df17387c3a7f5affdc1dd40ab91ecfae5e93bf532d4e3d4d98acead94"
debug_level = 1  # defatten, especially with LTO
tool_flags = {
    "LDFLAGS": ["-Wl,-rpath=/usr/lib/librewolf", "-Wl,-z,stack-size=2097152"]
}
env = {
    "SHELL": "/usr/bin/sh",
    "BUILD_OFFICIAL": "1",
    "MOZILLA_OFFICIAL": "1",
    "USE_SHORT_LIBNAME": "1",
    "MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE": "system",
    "MOZ_APP_REMOTINGNAME": "LibreWolf",
    "MOZ_NOSPAM": "1",
    # librewolf checks for it by calling --help
    "CBUILD_BYPASS_STRIP_WRAPPER": "1",
}
# FIXME: youtube causes crashes in libxul after some seconds
hardening = ["!int"]
# XXX: maybe someday
options = ["!cross", "!check"]

if self.profile().endian == "big":
    broken = "broken colors, needs patching, etc."

# crashes compiler in gl.c
if self.profile().arch == "riscv64":
    tool_flags["CXXFLAGS"] = ["-U_FORTIFY_SOURCE"]


def post_extract(self):
    self.cp(
        self.files_path / "stab.h", "toolkit/crashreporter/google-breakpad/src"
    )


def post_patch(self):
    from cbuild.util import cargo

    for crate in []:
        cargo.clear_vendor_checksums(self, crate, vendor_dir="third_party/rust")


def init_configure(self):
    from cbuild.util import cargo

    self.env["MOZBUILD_STATE_PATH"] = str(self.chroot_srcdir / ".mozbuild")
    self.env["AS"] = self.get_tool("CC")
    self.env["MOZ_MAKE_FLAGS"] = f"-j{self.make_jobs}"
    self.env["RUST_TARGET"] = self.profile().triplet
    # use all the cargo env vars we enforce
    self.env.update(cargo.get_environment(self))

def configure(self):
    conf_opts = [
        "--prefix=/usr",
        "--libdir=/usr/lib",
        "--host=" + self.profile().triplet,
        "--target=" + self.profile().triplet,
        "--disable-install-strip",
        "--disable-strip",
        "--enable-linker=lld",
        "--enable-optimize",
        "--enable-release",
        "--with-wasi-sysroot=/usr/wasm32-unknown-wasi",
        # we have our own flags and better
        "--disable-hardening",
        # system libs
        "--with-system-ffi",
        "--with-system-icu",
        "--with-system-jpeg",
        "--with-system-libevent",
        "--with-system-libvpx",
        "--with-system-nspr",
        "--with-system-nss",
        "--with-system-pixman",
        "--with-system-webp",
        "--with-system-zlib",
        # no apng support
        "--without-system-png",
        # features
        "--enable-audio-backends=pulseaudio",
        "--enable-dbus",
        "--enable-default-toolkit=cairo-gtk3-wayland",
        "--enable-ffmpeg",
        "--enable-jack",
        "--enable-necko-wifi",
        "--enable-pulseaudio",
        # disabled features
        "--disable-alsa",
        "--disable-jemalloc",
        "--disable-profiling",
        "--disable-tests",
        "--disable-updater",
        # browser options
        "--allow-addon-sideload",
        "--enable-application=browser",
        "--with-app-name=librewolf",
        "--with-branding=browser/branding/librewolf"
        "--with-distribution-id=org.chimera-linux", 
    ]

    match self.profile().arch:
        case "x86_64" | "aarch64":
            # broken with rust 1.78 as it enables packed_simd feature that uses removed platform_intrinsics
            # conf_opts += ["--enable-rust-simd"]
            pass

    if self.has_lto():
        conf_opts += ["--enable-lto=cross"]
        # configure for profiling
        self.log("bootstrapping profile...")
        with self.stamp("profile_configure") as s:
            s.check()
            self.log("configuring profile build...")
            self.do(
                "./mach",
                "configure",
                *conf_opts,
                "--enable-profile-generate=cross",
            )
        # do the profiling build
        with self.stamp("profile_build") as s:
            s.check()
            self.log("building profile build...")
            self.do("./mach", "build", "--priority", "normal")
        # package it
        with self.stamp("profile_package") as s:
            s.check()
            self.log("packaging profile build...")
            self.do("./mach", "package")
        # generate the profile data
        with self.stamp("profile_generate") as s:
            s.check()
            self.log("generating profile...")
            for d in self.cwd.glob("obj-*"):
                ldp = self.chroot_cwd / d.name / "dist/librewolf"
            self.do(
                "dbus-run-session",
                "--",
                "xvfb-run",
                "-s",
                "-screen 0 1920x1080x24",
                "./mach",
                "python",
                "./build/pgo/profileserver.py",
                env={
                    "HOME": str(self.chroot_cwd),
                    "JARLOG_FILE": str(self.chroot_cwd / "jarlog"),
                    "LD_LIBRARY_PATH": ldp,
                    "LIBGL_ALWAYS_SOFTWARE": "1",
                    "LLVM_PROFDATA": "llvm-profdata",
                    "XDG_RUNTIME_DIR": "/tmp",
                },
            )
        # clean up build dir
        with self.stamp("profile_clobber") as s:
            s.check()
            self.log("cleaning up profile build...")
            self.do("./mach", "clobber", "objdir")
        # and finally make use of this for real configure
        conf_opts += [
            "--enable-profile-use=cross",
            f"--with-pgo-profile-path={self.chroot_cwd / 'merged.profdata'}",
            f"--with-pgo-jarlog={self.chroot_cwd / 'jarlog'}",
        ]

    self.log("configuring final librewolf...")
    self.do("./mach", "configure", *conf_opts)


def build(self):
    self.do("./mach", "build", "--priority", "normal")


def install(self):
    self.do(
        "./mach",
        "install",
        env={"DESTDIR": str(self.chroot_destdir)},
    )

    self.install_file(
        "^/vendor.js", "usr/lib/librewolf/browser/defaults/preferences"
    )
    self.install_file("^/distribution.ini", "usr/lib/librewolf/distribution")
    self.install_file("^/librewolf.desktop", "usr/share/applications")

    # icons
    for sz in [16, 32, 48, 64, 128]:
        self.install_file(
            f"browser/branding/librewolf/default{sz}.png",
            f"usr/share/icons/hicolor/{sz}x{sz}/apps",
            name="librewolf.png",
        )

    # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
    self.uninstall("usr/lib/librewolf/librewolf-bin")
    self.install_link("usr/lib/librewolf/librewolf-bin", "librewolf")
