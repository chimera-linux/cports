import re


def clear_vendor_checksums(pkg, crate, vendor_dir="vendor"):
    p = pkg.cwd / vendor_dir / crate / ".cargo-checksum.json"
    p.write_text(re.sub(r"""("files":{)[^}]*""", r"\1", p.read_text()))


def write_vendor_checksum(pkg, crate, cksum, vendor_dir="vendor"):
    p = pkg.cwd / vendor_dir / crate / ".cargo-checksum.json"
    p.write_text(f'{{"files":{{}},"package":"{cksum}"}}')


def get_environment(pkg, jobs=None, cache=False):
    if not jobs:
        jobs = pkg.make_jobs

    sroot = pkg.profile().sysroot
    trip = pkg.profile().triplet
    utrip = trip.replace("-", "_").upper()

    env = {
        "CARGO_BUILD_TARGET": trip,
        f"CARGO_TARGET_{utrip}_LINKER": pkg.get_tool("CC"),
        "CARGO_BUILD_JOBS": str(jobs),
        "CARGO_PROFILE_RELEASE_PANIC": "abort",
        "CARGO_PROFILE_RELEASE_STRIP": "false",
        "CARGO_PROFILE_RELEASE_CODEGEN_UNITS": "1",
        "CARGO_REGISTRIES_CRATES_IO_PROTOCOL": "sparse",
        "CARGO_HOME": "/cbuild_cache/cargo" if cache else "/tmp",
        # gettext-rs
        "GETTEXT_BIN_DIR": "/usr/bin",
        "GETTEXT_LIB_DIR": str(sroot / "usr/lib/gettext"),
        # libgit2-sys
        "LIBGIT2_NO_VENDOR": "1",
        # libssh2-sys
        "LIBSSH2_SYS_USE_PKG_CONFIG": "1",
        # sodium-sys
        "SODIUM_USE_PKG_CONFIG": "1",
        # openssl-sys
        "OPENSSL_NO_VENDOR": "1",
        # pcre2-sys
        "PCRE2_SYS_STATIC": "0",
        # rustonig-sys
        "RUSTONIG_SYSTEM_LIBONIG": "1",
        # zstd-sys
        "ZSTD_SYS_USE_PKG_CONFIG": "1",
        # libsqlite3-sys
        "LIBSQLITE3_SYS_USE_PKG_CONFIG": "1",
        # cc-rs: make sure host compiler autoguess behavior is bypassed
        "HOST_CC": "clang",
        "HOST_CFLAGS": "-O2",
    }

    # the default of cargo is not to emit any debuginfo for --release
    # values >2 are also invalid
    # also, limit this to =1 for now. pretty much everything ever built with =0
    # so it's already a bonus, but with =2 the debuginfo is completely massive
    # also, putting this in regular rustflags is ignored for things that specify
    # things like
    # [profile.release.package.crate] strip = debuginfo
    # which will prioritize not generating anything, unless you use this var.
    # TODO: make this way less ugly by not copying _get_tool_flags logic,
    # but there's no way to reuse the debug value set here
    if (pkg.debug_level >= 1 or pkg.debug_level == -1) and pkg.options["debug"]:
        env["CARGO_PROFILE_RELEASE_DEBUG"] = "1"
    else:
        env["CARGO_PROFILE_RELEASE_DEBUG"] = "0"

    if pkg.profile().cross:
        env["PKG_CONFIG_ALLOW_CROSS"] = "1"

    if pkg.has_lto():
        if pkg.options["ltofull"]:
            env["CARGO_PROFILE_RELEASE_LTO"] = "fat"
        else:
            env["CARGO_PROFILE_RELEASE_LTO"] = "thin"

    return env


class Cargo:
    def __init__(self, tmpl, jobs=None, env={}, wrksrc=None):
        self.template = tmpl
        self.wrksrc = wrksrc
        self.env = env
        self.jobs = jobs

    def _invoke(
        self,
        command,
        args,
        jobs,
        offline,
        base_env,
        env,
        wrksrc,
        ewrapper,
        wrapper,
        stdout=None,
    ):
        tmpl = self.template

        if not jobs:
            jobs = self.jobs

        if not jobs:
            jobs = tmpl.make_jobs

        renv = get_environment(tmpl, jobs=jobs, cache=not offline)
        renv.update(tmpl.make_env)

        if base_env:
            renv.update(base_env)

        renv.update(self.env)
        renv.update(env)

        if not wrksrc:
            wrksrc = self.wrksrc
        if not wrksrc:
            wrksrc = tmpl.make_dir

        bargs = []
        if command == "vendor":
            bargs += ["--versioned-dirs", "--no-delete"]
        else:
            bargs += ["--target", tmpl.profile().triplet]

        if offline:
            bargs.append("--offline")

        # legacy config format to be avoided
        legacy = self.template.cwd / ".cargo/config"

        if legacy.is_file():
            self.template.error(
                "cargo: found legacy .cargo/config",
                hint="ensure .cargo/config.toml is used instead",
            )

        return self.template.do(
            *wrapper,
            *ewrapper,
            "cargo",
            command,
            *bargs,
            *args,
            env=renv,
            wrksrc=wrksrc,
            allow_network=not offline,
            stdout=stdout,
        )

    def invoke(
        self,
        command,
        args=[],
        jobs=None,
        offline=True,
        env={},
        wrksrc=None,
        wrapper=[],
    ):
        return self._invoke(
            command, args, jobs, offline, None, env, wrksrc, [], wrapper
        )

    def vendor(self, args=[], env={}, wrksrc=None, wrapper=[]):
        dirn = self.template.cwd
        if wrksrc is not None:
            dirn = dirn / wrksrc
        elif self.wrksrc is not None:
            dirn = dirn / self.wrksrc

        # Make sure to append in case a config is already present;
        # `parents` ensures the directory is allowed to exist already
        self.template.mkdir(dirn / ".cargo", parents=True)

        cfgp = dirn / ".cargo/config.toml"
        write_nl = cfgp.exists()

        with open(dirn / ".cargo/config.toml", "a") as outf:
            if write_nl:
                outf.write("\n")
                # we need to flush before passing to subprocess
                # or the newline does not get written properly
                outf.flush()

            return self._invoke(
                "vendor",
                args,
                1,
                False,
                None,
                env,
                wrksrc,
                [],
                wrapper,
                stdout=outf,
            )

    def build(
        self,
        args=[],
        command="build",
        jobs=None,
        env={},
        wrksrc=None,
        wrapper=[],
    ):
        tmpl = self.template
        return self._invoke(
            command,
            ["--release", *tmpl.make_build_args, *args],
            jobs,
            True,
            tmpl.make_build_env,
            env,
            wrksrc,
            tmpl.make_build_wrapper,
            wrapper,
        )

    def cbuild(
        self,
        args=[],
        command="cbuild",
        jobs=None,
        env={},
        wrksrc=None,
        wrapper=[],
    ):
        return self.build(
            [
                "--prefix",
                "/usr",
                "--library-type",
                "cdylib",
                "--library-type",
                "staticlib",
                *args,
            ],
            command,
            jobs,
            env,
            wrksrc,
            wrapper,
        )

    def install(
        self,
        args=[],
        command="install",
        jobs=None,
        env={},
        wrksrc=None,
        wrapper=[],
    ):
        tmpl = self.template
        retv = self._invoke(
            command,
            [
                "--root",
                str(tmpl.chroot_destdir / "usr"),
                "--path",
                ".",
                "--no-track",
                *tmpl.make_install_args,
                *args,
            ],
            jobs,
            True,
            tmpl.make_install_env,
            env,
            wrksrc,
            tmpl.make_install_wrapper,
            wrapper,
        )
        return retv

    def cinstall(
        self,
        args=[],
        command="cinstall",
        jobs=None,
        env={},
        wrksrc=None,
        wrapper=[],
    ):
        tmpl = self.template
        retv = self._invoke(
            command,
            [
                "--prefix",
                "/usr",
                "--library-type",
                "cdylib",
                "--library-type",
                "staticlib",
                "--destdir",
                str(tmpl.chroot_destdir),
                *tmpl.make_install_args,
                *args,
            ],
            jobs,
            True,
            tmpl.make_install_env,
            env,
            wrksrc,
            tmpl.make_install_wrapper,
            wrapper,
        )
        return retv

    def check(
        self,
        args=[],
        command="test",
        jobs=None,
        env={},
        wrksrc=None,
        wrapper=[],
    ):
        tmpl = self.template
        return self._invoke(
            command,
            tmpl.make_check_args + args,
            jobs,
            True,
            tmpl.make_check_env,
            env,
            wrksrc,
            tmpl.make_check_wrapper,
            wrapper,
        )
